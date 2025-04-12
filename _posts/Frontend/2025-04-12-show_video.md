---
categories: [Frontend]
tags: [Frontend, Video]
layout: none
---

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>小毛驴&小黄狗</title>
    <style>
        /* 默认样式（适用于 PC） */
        video {
            width: 640px;
            height: 360px;
        }

        /* 针对手机的样式 */
        @media (max-width: 768px) {
            video {
                width: 100%;
                height: auto;
            }
        }
    </style>

</head>
<body>
    <central><h1>小黄狗笑得很开心</h1></central>

    <!-- 使用 video 标签嵌入视频 -->
    <video controls autoplay muted>
        <source src="{{ '/assets/videos/donkey_dog.mp4' | relative_url }}" type="video/mp4">
        您的浏览器不支持 video 标签。
    </video>

</body>
