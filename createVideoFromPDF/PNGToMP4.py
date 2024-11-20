from moviepy.editor import ImageClip

# Görüntü dosyasının yolu
image_path = "image.png"

# Çıkış videosunun yolu
output_video_path = "output_video.mp4"

# Görüntüden video oluştur
clip = ImageClip(image_path, duration=5)  # 5 saniyelik video
clip.write_videofile(output_video_path, fps=24, codec="libx264")

print(f"Video başarıyla oluşturuldu: {output_video_path}")
