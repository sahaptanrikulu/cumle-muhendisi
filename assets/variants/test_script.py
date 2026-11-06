import os
import subprocess

out_dir = "C:/Users/sahap/Downloads/Hermes/cumle-muhendisi/assets/variants"
os.makedirs(out_dir, exist_ok=True)

chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"

# -------------------------------------------------------------
# VARIANT 1: Cyber-Blueprint (Linear / Raycast Dark Style)
# -------------------------------------------------------------
html_v1 = """<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    width: 1600px; height: 900px;
    background: #080C14;
    background-image: 
      radial-gradient(circle at 50% 0%, rgba(56, 189, 248, 0.15) 0%, transparent 50%),
      radial-gradient(circle at 85% 90%, rgba(99, 102, 241, 0.12) 0%, transparent 40%),
      linear-gradient(rgba(255, 255, 255, 0.03) 1px, transparent 1px),
      linear-gradient(90deg, rgba(255, 255, 255, 0.03) 1px, transparent 1px);
    background-size: 100% 100%, 100% 100%, 40px 40px, 40px 40px;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    color: #F8FAFC;
    padding: 50px 70px;
    display: flex; flex-direction: column; justify-content: space-between;
  }
  .header { display: flex; justify-content: space-between; align-items: center; }
  .logo-box { display: flex; align-items: center; gap: 18px; }
  .icon-glow {
    width: 54px; height: 54px; border-radius: 14px;
    background: linear-gradient(135deg, #0284C7, #4F46E5);
    display: flex; align-items: center; justify-content: center;
    box-shadow: 0 0 25px rgba(56, 189, 248, 0.5);
  }
  .title { font-size: 34px; font-weight: 800; letter-spacing: -0.5px; }
  .badge-glow {
    background: rgba(56, 189, 248, 0.1); border: 1px solid rgba(56, 189, 248, 0.3);
    color: #38BDF8; padding: 6px 16px; border-radius: 9999px; font-size: 13px; font-weight: 700;
  }
  .cards-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin: 30px 0; }
  .card {
    background: rgba(15, 23, 42, 0.7); backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 18px; padding: 30px;
  }
  .card-before { border-color: rgba(239, 68, 68, 0.3); box-shadow: 0 0 30px rgba(239, 68, 68, 0.08); }
  .card-after { border-color: rgba(16, 185, 129, 0.4); box-shadow: 0 0 35px rgba(16, 185, 129, 0.12); }
  .tag { font-size: 12px; font-weight: 800; padding: 4px 12px; border-radius: 6px; text-transform: uppercase; display: inline-block; margin-bottom: 15px; }
  .tag-red { background: rgba(239, 68, 68, 0.2); color: #F87171; border: 1px solid rgba(239, 68, 68, 0.3); }
  .tag-green { background: rgba(16, 185, 129, 0.2); color: #34D399; border: 1px solid rgba(16, 185, 129, 0.3); }
  .diff-box { background: rgba(0,0,0,0.4); border-radius: 10px; padding: 16px; font-size: 15px; line-height: 1.6; margin-bottom: 20px; font-family: monospace; }
  .list-item { display: flex; gap: 12px; font-size: 15px; line-height: 1.5; color: #94A3B8; margin-bottom: 12px; }
  .footer { display: flex; justify-content: space-between; align-items: center; border-top: 1px solid rgba(255, 255, 255, 0.08); padding-top: 20px; color: #64748B; font-size: 14px; }
</style>
</head>
<body>
  <div class="header">
    <div class="logo-box">
      <div class="icon-glow">⚡</div>
      <div>
        <div class="title">CÜMLE MÜHENDİSİ <span style="font-size:16px; color:#38BDF8; font-weight:600;">v2.0</span></div>
        <div style="font-size:14px; color:#64748B;">TÜRKÇE İÇİN DİL VE SENTAKS MOTORU</div>
      </div>
    </div>
    <div class="badge-glow">● DETERMINISTIC AST & RHYTHM ENGINE</div>
  </div>
  <div class="cards-grid">
    <div class="card card-before">
      <div class="tag tag-red">HAM YAPAY ZEKA MODELİ</div>
      <div class="diff-box" style="color:#FCA5A5; border-left:3px solid #EF4444;">
        - "Şirketimiz dijital dönüşüm kapsamında önemli bir adım atmaktadır ve bulut altyapımızın kurulması süreçlerin yürütülmesine katkı sağlamaktadır..."
      </div>
      <div class="list-item"><span style="color:#EF4444;">✕</span> Saatin tiktakı gibi 15-20 kelimelik mekanik cümle ritmi</div>
      <div class="list-item"><span style="color:#EF4444;">✕</span> İngilizce SVO kopyası, lafı arkadan dolandıran yan cümleler</div>
      <div class="list-item"><span style="color:#EF4444;">✕</span> Kof yardımcı fiiller ("gerçekleştirmek", "katkı sağlamak")</div>
      <div class="list-item"><span style="color:#EF4444;">✕</span> Sonu gelmeyen -mektedir / -maktadır bürokrasi kuruluğu</div>
    </div>
    <div class="card card-after">
      <div class="tag tag-green">CÜMLE MÜHENDİSİ ÇIKTISI</div>
      <div class="diff-box" style="color:#6EE7B7; border-left:3px solid #10B981;">
        + "Şirket içi dijital altyapımızı buluta taşıyarak günlük işlerimizi çok daha hızlı ve pürüzsüz yürütmeye başladık."
      </div>
      <div class="list-item"><span style="color:#10B981;">✓</span> Kısa hüküm cümleleri ile ulaçlı akıcı uzun cümle harmanı</div>
      <div class="list-item"><span style="color:#10B981;">✓</span> Doğrudan hedefe bağlanan sola dallı öz Türkçe mimarisi</div>
      <div class="list-item"><span style="color:#10B981;">✓</span> Şişkin laflardan arınmış doğrudan güçlü ve aktif eylemler</div>
      <div class="list-item"><span style="color:#10B981;">✓</span> Olgusal sadakat: Gerçek verileri ve teknik terimleri koruma</div>
    </div>
  </div>
  <div class="footer">
    <div>⚡ %100 Açık Kaynak • Yerel Çalışma • MIT Lisansı</div>
    <div style="color:#94A3B8; font-weight:600;">github.com/sahaptanrikulu/cumle-muhendisi</div>
  </div>
</body>
</html>"""

with open(f"{out_dir}/variant_1.html", "w", encoding="utf-8") as f:
    f.write(html_v1)

print("Variant 1 written.")
