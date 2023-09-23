---
categories: [Python]
tags: Python DL
---

# 写在前面

前几天改了一份代码, 是关于深度学习中卷积神经网络的Python代码, 用于解决分类问题. 代码是用TensorFlow的Keras接口写的, 需求是转换成pytorch代码, 鉴于两者的api相近, 盖起来也不会太难, 就是一些细节需要注意, 在这里记录一下, 方便大家参考. 



# 关于库函数导入

首先来看看在库函数的导入方面这两个流行的深度学习框架有什么区别, 这就需要简单了解一下二者的主要结构了. 为方便叙述, 下面提到的TF都是指TensorFlow2.X with Keras, Torch都是指PyTorch.

## 模型构建

首先来看模型的构建, 对于TF, 模型的构建可以方便地通过`sequential`方法得到, 这就需要引入该方法:

```python
from tensorflow.keras.models import Sequential
```

在Torch中, 当然也可以通过`sequential`进行模型的构建, (不过官方还是更推荐采用面向对象的方式)

这里需要引入:

```python
from torch.nn import Sequential
```



说到模型构建, 就不得不提在卷积神经网络里面十分常用的几个层: conv层, maxpool层和全连接层(softmax), 这些在两个框架中都有现成的, 下面来看看如何调用这些方法:

在TF中:

```python
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import Activation, Dropout, Flatten, Dense
```

而在Torch中:

```python
from torch.nn import Conv2d, MaxPool2d
from torch.nn import Flatten, Linear, CrossEntropyLoss
from torch.optim import SGD
```

可见二者只有些微的不同, TF中将一些激活函数的调用放在了参数里面, 而Torch都是以库函数的形式给出的. 

## 数据读入

最后来看看数据的导入部分, 在TF中可以很方便地使用下面的方法进行数据(图片)的处理和读取:

```python
from tensorflow.keras import backend
from tensorflow.keras.preprocessing.image import ImageDataGenerator
```

在Torch中, 需要类似导入:

```python
from torchvision import transforms, datasets
from torch.utils.data import DataLoader
```



# 数据读取/处理部分的api差异

在数据读取部分, 我感觉还是Keras比较方便一些[^1], Torch主要还是使用的模块化的导入方式, 需要先实例化一个类, 然后用该对象进行对图像的处理. 

下面先来看看TF的读取图片数据的代码:

```python
# 导入数据
if backend.image_data_format() == 'channels_first':
    input_shape = (3, img_width, img_height)
else:
    input_shape = (img_width, img_height, 3)

# 训练集图像增强
train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

# 测试集图像增强（only rescaling）
test_datagen = ImageDataGenerator(rescale=1. / 255)

train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='categorical')  # 多分类

validation_generator = test_datagen.flow_from_directory(
    validation_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='categorical')  # 多分类
```



接下来是Torch的代码:

```python
# 导入数据
input_shape = (img_width, img_height, 3)

# 训练集图像增强
train_datagen = transforms.Compose([
    transforms.ToTensor(),
    transforms.RandomHorizontalFlip(),
    transforms.Resize((img_width, img_height))
])


# 测试集图像增强（only rescaling）
test_datagen = transforms.Compose([  # 对读取的图片进行以下指定操作
    transforms.ToTensor(), # 这步相当于Keras的rescale为1/255
    transforms.Resize((img_width, img_height))
])

train_generator = datasets.ImageFolder(train_data_dir, 
                                       transform=train_datagen)

validation_generator = datasets.ImageFolder(validation_data_dir,
                                            transform=test_datagen)

train_loader = torch.utils.data.DataLoader(train_generator, 
                                           batch_size=batch_size,
                                           shuffle=True)

test_loader = torch.utils.data.DataLoader(validation_generator,
                                          batch_size=batch_size,
                                          shuffle=False)
```



# 模型构建部分的api差异

下面谈谈最重要的, 模型的构建部分的api调用的区别, 在TF中直接进行`model.add`的调用, 就可以方便地创建一个CNN识别模型了, 这里需要注意数据流维度的对应, 下面是代码. 简练直观.

```python
# 创建模型
model = Sequential()
model.add(Conv2D(filters=6, 
                 kernel_size=(5, 5), 
                 padding='valid', 
                 input_shape=input_shape, 
                 activation='tanh'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(filters=16, 
                 kernel_size=(5, 5), 
                 padding='valid', 
                 activation='tanh'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(120, activation='tanh'))
model.add(Dense(84, activation='tanh'))
model.add(Dense(4, activation='softmax'))

#编译模型
model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])
```

在Torch中, 也有类似的方法, 不过不需要进行模型的编译, 代码如下:

```python
# 创建模型
model = Sequential(
    Conv2d(in_channels=3, 
           out_channels=6, 
           kernel_size=(5, 5), 
           padding='valid'),
    MaxPool2d(kernel_size=(2, 2)),
    Conv2d(in_channels=6, 
           out_channels=16, 
           kernel_size=(5, 5), 
           padding='valid'),
    MaxPool2d(kernel_size=(2, 2)),
    Flatten(),
    Linear(400, 120),
    Linear(120, 84), 
    Linear(84, 4)
)

# 这里设置了损失函数为交叉熵函数
criterion = CrossEntropyLoss()
# 设置优化器为随机梯度下降算法
optimizer = SGD(model.parameters(), lr=0.001)
```

这里在api方面还是有一些区别, 例如全连接层的写法以及参数, 还有卷积层的一些区别. 一样地, 还是要非常注意数据维度. 

# 模型训练部分的api差异

在TF中, 由于引入了Keras这个强有力而且语法简洁的api, 训练起来模型也十分简单, 代码如下: 

```python
#训练模型
history=model.fit_generator(
    train_generator,
    steps_per_epoch=nb_train_samples // batch_size,
    epochs=epochs,
    validation_data=validation_generator,
    validation_steps=nb_validation_samples // batch_size)
```



但是在Torch中, 还需要自己一步步进行搭建, 略显繁琐

```python
n_total_steps = len(train_loader)
for epoch in range(num_epochs):
    for i, (images, labels) in enumerate(train_loader):
        # Forward pass
        outputs = model(images)
        loss = criterion(outputs, labels)
        # Backward and optimize
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if (i+1) % 5 == 0:
            print(f'''
            Epoch [{epoch+1}/{num_epochs}], 
            Step [{i+1}/{n_total_steps}], 
            Loss: {loss.item():.4f}
            ''')

torch.save(model.state_dict(), './ckpt')
```

# 小结

善用搜索引擎, 官方文档都有这两个框架的详细api使用方法. 



# 主要参考

[^1]:[图像预处理 - Keras 中文文档](https://keras.io/zh/preprocessing/image/);
