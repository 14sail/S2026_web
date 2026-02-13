import os
import json

# 設定
IMAGE_DIR = 'images'
DATA_FILE = 'data.json'
# 預設分類關鍵字（不分大小寫）
CATEGORIES = ['About', 'Life', 'Camping']

def get_category(folder_name):
    """根據資料夾名稱判斷分類"""
    name_lower = folder_name.lower()
    for cat in CATEGORIES:
        if cat.lower() in name_lower:
            return cat
    return "Life"  # 找不到關鍵字時，預設歸類到 Life

def format_title(folder_name):
    """將資料夾名稱轉為漂亮的標題 (例如 life_2025s2 -> Life 2025 S2)"""
    return folder_name.replace('_', ' ').title()

def update_gallery():
    if not os.path.exists(IMAGE_DIR):
        print(f"❌ 找不到 {IMAGE_DIR} 資料夾")
        return

    albums = []
    
    # 掃描 images 內的所有子資料夾
    folders = [f for f in os.listdir(IMAGE_DIR) if os.path.isdir(os.path.join(IMAGE_DIR, f))]
    
    # 排序，讓最新的相簿在前面
    folders.sort(reverse=True)

    for folder in folders:
        folder_path = os.path.join(IMAGE_DIR, folder)
        # 抓取圖片檔案
        valid_extensions = ('.jpg', '.jpeg', '.png', '.webp', '.JPG', '.PNG')
        photos = [
            f"images/{folder}/{img}" 
            for img in os.listdir(folder_path) 
            if img.endswith(valid_extensions)
        ]
        
        if photos:
            # 排序照片檔名
            photos.sort()
            
            albums.append({
                "title": format_title(folder),
                "category": get_category(folder),
                "photos": photos
            })

    # 寫入 data.json
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump({"albums": albums}, f, ensure_ascii=False, indent=2)

    print(f"✅ 更新完成！共偵測到 {len(albums)} 個相簿。")
    print(f"📁 已更新至 {DATA_FILE}")

if __name__ == "__main__":
    update_gallery()