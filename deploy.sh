#!/bin/bash
echo "🚀 開始自動更新攝影集..."
python3 update_data.py
git add .
git commit -m "Update gallery: $(date +'%Y-%m-%d %H:%M:%S')"
git push
echo "✨ 全部完成！網頁將在 1 分鐘後更新。"