#!/usr/bin/env python3
# 图片合成脚本：3x3布局，客厅图占2x2，其余5张各占1x1

from PIL import Image
import os

# 图片路径配置
IMAGE_DIR = "public/images/"
OUTPUT_PATH = "public/images/course_poster.jpg"

# 图片顺序：按3x3网格排列
# 位置：(行, 列)
# (0,0) 客厅图 (2x2)  (0,2) 图1
# (1,2) 图2
# (2,0) 图3        (2,1) 图4  (2,2) 图5
IMAGE_FILES = [
    "d33aa187-5823-4030-a7f1-85efb9421c8d.jpg",  # 0,0: 主图 (2x2)
    "ad0d3a86-7c2b-4f96-b029-ad3b31616f24.jpg",  # 0,2
    "87352117-ac05-4758-b2b5-a3983cc9b6ec.jpg",  # 1,2
    "ed91f7a1-d1bf-4384-ae46-ef620ea20ed5.jpg",  # 2,0
    "course-schedule.jpg",                        # 2,1
    "price-list.jpg"                              # 2,2
]

# 输出配置
TILE_SIZE = 400  # 每个格子的大小（像素）
BORDER_SIZE = 10  # 图片之间的边框大小
BORDER_COLOR = (255, 255, 255)  # 白色边框
BACKGROUND_COLOR = (255, 255, 255)  # 背景色

def create_composite():
    # 计算输出图片大小：3x3格子 + 边框
    total_size = 3 * TILE_SIZE + 4 * BORDER_SIZE
    output = Image.new('RGB', (total_size, total_size), BACKGROUND_COLOR)
    
    # 加载所有图片
    images = []
    for img_file in IMAGE_FILES:
        img_path = os.path.join(IMAGE_DIR, img_file)
        try:
            img = Image.open(img_path)
            images.append(img)
            print(f"✅ 加载图片: {img_file}")
        except Exception as e:
            print(f"❌ 加载失败 {img_file}: {e}")
            return False
    
    if len(images) != 6:
        print(f"❌ 需要6张图片，实际加载了{len(images)}张")
        return False
    
    # 粘贴主图 (2x2 位置：0,0)
    main_img = images[0].resize((2 * TILE_SIZE + BORDER_SIZE, 2 * TILE_SIZE + BORDER_SIZE), Image.Resampling.LANCZOS)
    output.paste(main_img, (BORDER_SIZE, BORDER_SIZE))
    print("🖼️  粘贴主图 (2x2)")
    
    # 粘贴 (0,2) 位置图片
    img1 = images[1].resize((TILE_SIZE, TILE_SIZE), Image.Resampling.LANCZOS)
    x = 2 * TILE_SIZE + 3 * BORDER_SIZE
    y = BORDER_SIZE
    output.paste(img1, (x, y))
    print("🖼️  粘贴图片到 (0,2)")
    
    # 粘贴 (1,2) 位置图片
    img2 = images[2].resize((TILE_SIZE, TILE_SIZE), Image.Resampling.LANCZOS)
    x = 2 * TILE_SIZE + 3 * BORDER_SIZE
    y = TILE_SIZE + 2 * BORDER_SIZE
    output.paste(img2, (x, y))
    print("🖼️  粘贴图片到 (1,2)")
    
    # 粘贴 (2,0) 位置图片
    img3 = images[3].resize((TILE_SIZE, TILE_SIZE), Image.Resampling.LANCZOS)
    x = BORDER_SIZE
    y = 2 * TILE_SIZE + 3 * BORDER_SIZE
    output.paste(img3, (x, y))
    print("🖼️  粘贴图片到 (2,0)")
    
    # 粘贴 (2,1) 位置图片
    img4 = images[4].resize((TILE_SIZE, TILE_SIZE), Image.Resampling.LANCZOS)
    x = TILE_SIZE + 2 * BORDER_SIZE
    y = 2 * TILE_SIZE + 3 * BORDER_SIZE
    output.paste(img4, (x, y))
    print("🖼️  粘贴图片到 (2,1)")
    
    # 粘贴 (2,2) 位置图片
    img5 = images[5].resize((TILE_SIZE, TILE_SIZE), Image.Resampling.LANCZOS)
    x = 2 * TILE_SIZE + 3 * BORDER_SIZE
    y = 2 * TILE_SIZE + 3 * BORDER_SIZE
    output.paste(img5, (x, y))
    print("🖼️  粘贴图片到 (2,2)")
    
    # 保存输出
    output.save(OUTPUT_PATH, quality=95, optimize=True)
    print(f"\n🎉 合成完成！输出文件: {OUTPUT_PATH}")
    print(f"📏 图片尺寸: {total_size}x{total_size} 像素")
    
    return True

if __name__ == "__main__":
    print("🎨 开始合成3x3布局海报...")
    print("=" * 50)
    
    # 安装Pillow库
    try:
        from PIL import Image
    except ImportError:
        print("🔧 正在安装Pillow库...")
        os.system("pip install pillow --break-system-packages")
        from PIL import Image
    
    create_composite()
