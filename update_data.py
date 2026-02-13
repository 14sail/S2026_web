import os
import json

# 設定
IMAGE_DIR = 'images'
DATA_FILE = 'data.json'
# 預設分類關鍵字
CATEGORIES = ['Life', 'About', 'Camping']

def get_category(folder_name):
    """根據資料夾名稱判斷分類"""
    name_lower = folder_name.lower()
    for cat in CATEGORIES:
        if cat.lower() in name_lower:
            return cat
    return "Life"

def format_title(folder_name):
    """
    修改後的標題邏輯：
    只保留年份與季度（例如 2025S2），移除 Life, Camping, About 等字眼。
    """
    title = folder_name.lower()
    # 移除分類關鍵字與底線
    for cat in CATEGORIES:
        title = title.replace(cat.lower(), "")
    
    title = title.replace('_', '').replace('-', '').strip()
    
    # 將結果轉為大寫（例如 2025s2 -> 2025S2）
    return title.upper()

def update_gallery():
    if not os.path.exists(IMAGE_DIR):
        print(f"❌ 找不到 {IMAGE_DIR} 資料夾")
        return

    albums = []
    
    # 掃描 images 內的所有子資料夾
    if not os.path.exists(IMAGE_DIR): return
    folders = [f for f in os.listdir(IMAGE_DIR) if os.path.isdir(os.path.join(IMAGE_DIR, f))]
    
    # 排序
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
            photos.sort()
            
            albums.append({
                "title": format_title(folder), # 這裡會產生 2025S2
                "category": get_category(folder),
                "photos": photos
            })

    # 寫入 data.json
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump({"albums": albums}, f, ensure_ascii=False, indent=2)

    print(f"✅ 更新完成！標題已統一為年季格式（如：2025S2）。")

if __name__ == "__main__":
    update_gallery()