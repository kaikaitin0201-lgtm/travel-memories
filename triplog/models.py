# -*- coding: utf-8 -*-
from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

class Prefecture(models.Model):
    name = models.CharField(max_length=10, unique=True)
    visit_date = models.CharField(max_length=50, blank=True)
    is_home = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Photo(models.Model):
    prefecture = models.ForeignKey(Prefecture, on_delete=models.CASCADE, related_name='photos')
    # 元の高画質画像を保存する場所
    image = models.ImageField(upload_to='trip_photos/')
    # ↓ 追加：サムネイル（縮小版）を保存する場所
    thumbnail = models.ImageField(upload_to='trip_photos/thumbnails/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    # 保存される瞬間に、自動でサムネイルを作る魔法の処理
    def save(self, *args, **kwargs):
        # サムネイルがまだ無くて、元画像がある場合のみ実行
        if not self.thumbnail and self.image:
            img = Image.open(self.image)
            # 色の形式を整える
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            # 画質を保ったまま、最大400x400サイズに縮小
            img.thumbnail((400, 400), Image.Resampling.LANCZOS)
            
            # メモリ上に一時保存
            output = BytesIO()
            img.save(output, format='JPEG', quality=85)
            output.seek(0)
            
            # サムネイルとしてセット
            file_name = f"thumb_{self.image.name.split('/')[-1].split('.')[0]}.jpg"
            self.thumbnail = InMemoryUploadedFile(
                output, 'ImageField', file_name,
                'image/jpeg', sys.getsizeof(output), None
            )
        super().save(*args, **kwargs)