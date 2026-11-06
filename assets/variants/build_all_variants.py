import os
import subprocess
import time

variants_dir = "C:/Users/sahap/Downloads/Hermes/cumle-muhendisi/assets/variants"
os.makedirs(variants_dir, exist_ok=True)
chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"

# ==============================================================================
# DEFINITIONS FOR 10 DISTINCT VARIANTS
# ==============================================================================

variants = {}

# ------------------------------------------------------------------------------
# 1. Cyber-Blueprint (Dark Linear / Raycast Style)
# ------------------------------------------------------------------------------
variants[1] = {
    "title": "Cyber-Blueprint (Dark Linear)",
    "html": """<!DOCTYPE html>
<html lang="tr"><head><meta charset="UTF-8">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    width: 1600px; height: 900px; background: #080C14;
    background-image: 
      radial-gradient(circle at 50% 0%, rgba(56, 189, 248, 0.18) 0%, transparent 60%),
      radial-gradient(circle at 90% 90%, rgba(99, 102, 241, 0.15) 0%, transparent 50%),
      linear-gradient(rgba(255, 255, 255, 0.04) 1px, transparent 1px),
      linear-gradient(90deg, rgba(255, 255, 255, 0.04) 1px, transparent 1px);
    background-size: 100% 100%, 100% 100%, 40px 40px, 40px 40px;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    color: #F8FAFC; padding: 48px 64px; display: flex; flex-direction: column; justify-content: space-between;
  }
  .header { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.08); padding-bottom: 24px; }
  .logo { display: flex; align-items: center; gap: 16px; }
  .logo-box { width: 50px; height: 50px; border-radius: 12px; background: linear-gradient(135deg, #0284C7, #6366F1); display: flex; align-items: center; justify-content: center; font-size: 24px; box-shadow: 0 0 25px rgba(56,189,248,0.5); }
  .h1 { font-size: 32px; font-weight: 800; letter-spacing: -0.5px; }
  .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 28px; margin: 24px 0; }
  .card { background: rgba(15, 23, 42, 0.75); backdrop-filter: blur(20px); border: 1.5px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 28px; }
  .card-before { border-color: rgba(239, 68, 68, 0.4); box-shadow: 0 0 30px rgba(239, 68, 68, 0.1); }
  .card-after { border-color: rgba(16, 185, 129, 0.4); box-shadow: 0 0 35px rgba(16, 185, 129, 0.15); }
  .pill { font-size: 12px; font-weight: 800; padding: 5px 12px; border-radius: 6px; letter-spacing: 0.5px; display: inline-block; margin-bottom: 14px; }
  .pill-r { background: rgba(239,68,68,0.2); color: #F87171; border: 1px solid rgba(239,68,68,0.4); }
  .pill-g { background: rgba(16,185,129,0.2); color: #34D399; border: 1px solid rgba(16,185,129,0.4); }
  .code-box { background: rgba(0,0,0,0.5); border-radius: 10px; padding: 16px; font-size: 14.5px; line-height: 1.5; margin-bottom: 18px; font-family: ui-monospace, monospace; }
  .item { display: flex; gap: 12px; font-size: 14.5px; color: #94A3B8; margin-bottom: 10px; }
  .bento { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; }
  .b-item { background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 14px 18px; font-size: 13px; color: #94A3B8; }
  .b-item strong { display: block; color: #F8FAFC; font-size: 14px; margin-bottom: 3px; }
  .footer { display: flex; justify-content: space-between; align-items: center; border-top: 1px solid rgba(255,255,255,0.08); padding-top: 18px; color: #64748B; font-size: 13.5px; }
</style>
</head><body>
  <div class="header">
    <div class="logo">
      <div class="logo-box">⚡</div>
      <div>
        <div class="h1">CÜMLE MÜHENDİSİ <span style="font-size:15px; color:#38BDF8; font-weight:600; background:rgba(56,189,248,0.15); padding:3px 8px; border-radius:6px; margin-left:8px;">v2.0</span></div>
        <div style="font-size:13.5px; color:#64748B; font-weight:500;">TÜRKÇE İÇİN DİL VE SENTAKS MOTORU</div>
      </div>
    </div>
    <div style="background:rgba(56,189,248,0.1); border:1px solid rgba(56,189,248,0.3); color:#38BDF8; padding:8px 18px; border-radius:9999px; font-size:13px; font-weight:700;">● DETERMINISTIC AST & RHYTHM ENGINE</div>
  </div>
  <div class="grid">
    <div class="card card-before">
      <div class="pill pill-r">ÖNCE: HAM YAPAY ZEKA ÇIKTISI</div>
      <div class="code-box" style="color:#FCA5A5; border-left:3px solid #EF4444;">
        - "Şirketimiz dijital dönüşüm kapsamında önemli bir adım atmaktadır ve bulut altyapımızın kurulması süreçlerin yürütülmesine katkı sağlamaktadır..."
      </div>
      <div class="item"><span style="color:#EF4444;">✕</span> Saatin tiktakı gibi hep aynı boyda (15-20 kelime) tekdüzelik</div>
      <div class="item"><span style="color:#EF4444;">✕</span> İngilizceden miras kalan, lafı arkasından dolandıran yapı</div>
      <div class="item"><span style="color:#EF4444;">✕</span> Kof yardımcı fiiller ("gerçekleştirmek", "katkı sağlamak")</div>
      <div class="item"><span style="color:#EF4444;">✕</span> Sonu gelmeyen -mektedir / -maktadır bürokrasi kuruluğu</div>
    </div>
    <div class="card card-after">
      <div class="pill pill-g">SONRA: CÜMLE MÜHENDİSİ ÇIKTISI</div>
      <div class="code-box" style="color:#6EE7B7; border-left:3px solid #10B981;">
        + "Şirket içi dijital altyapımızı buluta taşıyarak günlük işlerimizi çok daha hızlı ve pürüzsüz yürütmeye başladık."
      </div>
      <div class="item"><span style="color:#10B981;">✓</span> Kısa hüküm cümleleri ile ulaçlı akıcı uzun cümle harmanı</div>
      <div class="item"><span style="color:#10B981;">✓</span> Doğrudan hedefe bağlanan sola dallı öz Türkçe mimarisi</div>
      <div class="item"><span style="color:#10B981;">✓</span> Şişkin laflardan arınmış doğrudan güçlü ve aktif eylemler</div>
      <div class="item"><span style="color:#10B981;">✓</span> Olgusal sadakat: Gerçek verileri ve teknik terimleri koruma</div>
    </div>
  </div>
  <div class="bento">
    <div class="b-item"><strong>📐 Öz Türkçe Sentaksı</strong>İngilizce çeviri kalıplarını ulaç sistemiyle yıkar.</div>
    <div class="b-item"><strong>⚡ 100+ Klişe Temizliği</strong>Yapay zeka ezberlerini ve dolgu lafları budar.</div>
    <div class="b-item"><strong>🛡️ Teknik Terim Sadakati</strong>SDI, NFPA gibi endüstri standartlarını korur.</div>
    <div class="b-item"><strong>📊 CLI Analiz Aracı</strong>Terminalden deterministik CoV denetimi yapar.</div>
  </div>
  <div class="footer">
    <div>⚡ %100 Açık Kaynak • Tamamen Yerel ve Güvenli • MIT Lisansı</div>
    <div style="color:#94A3B8; font-weight:600;">github.com/sahaptanrikulu/cumle-muhendisi</div>
  </div>
</body></html>"""
}

# ------------------------------------------------------------------------------
# 2. Editorial Broadsheet (Gazete & Kırmızı Kalem Edisyonu)
# ------------------------------------------------------------------------------
variants[2] = {
    "title": "Editorial Broadsheet (Gazete & Kırmızı Kalem)",
    "html": """<!DOCTYPE html>
<html lang="tr"><head><meta charset="UTF-8">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    width: 1600px; height: 900px; background: #F6F3EB;
    font-family: "Georgia", "Times New Roman", serif;
    color: #1C1917; padding: 48px 64px; display: flex; flex-direction: column; justify-content: space-between;
  }
  .header { border-bottom: 3px double #1C1917; padding-bottom: 20px; display: flex; justify-content: space-between; align-items: flex-end; }
  .h1 { font-size: 54px; font-weight: 900; letter-spacing: -1px; text-transform: uppercase; line-height: 1; }
  .sub { font-size: 15px; font-family: -apple-system, sans-serif; font-weight: 600; color: #78716C; margin-top: 6px; letter-spacing: 1px; }
  .stamp { border: 2.5px solid #DC2626; color: #DC2626; padding: 6px 14px; border-radius: 4px; font-family: -apple-system, sans-serif; font-weight: 900; font-size: 14px; transform: rotate(-3deg); }
  .main-stage { display: grid; grid-template-columns: 1fr 1fr; gap: 40px; margin: 26px 0; }
  .paper-col { background: #FFFFFF; border: 1px solid #E7E5E4; box-shadow: 4px 6px 0 rgba(0,0,0,0.06); padding: 32px; border-radius: 4px; position: relative; }
  .col-head { font-family: -apple-system, sans-serif; font-size: 13px; font-weight: 800; letter-spacing: 1px; text-transform: uppercase; padding-bottom: 12px; border-bottom: 1px solid #E7E5E4; margin-bottom: 18px; display: flex; justify-content: space-between; }
  .strike-box { font-size: 17px; line-height: 1.6; color: #78716C; margin-bottom: 22px; font-style: italic; }
  .strike-box span.del { text-decoration: line-through; color: #DC2626; font-weight: bold; background: #FEE2E2; }
  .clean-box { font-size: 18px; line-height: 1.6; color: #1C1917; margin-bottom: 22px; font-weight: 500; }
  .notes { font-family: -apple-system, sans-serif; font-size: 14px; line-height: 1.5; color: #44403C; display: flex; flex-direction: column; gap: 8px; }
  .notes li { list-style: none; display: flex; gap: 8px; }
  .footer { border-top: 1px solid #1C1917; padding-top: 18px; font-family: -apple-system, sans-serif; font-size: 13.5px; display: flex; justify-content: space-between; color: #78716C; }
</style>
</head><body>
  <div class="header">
    <div>
      <div class="h1">Cümle Mühendisi</div>
      <div class="sub">YAPAY ZEKA YAZIMINI İNSAN KALEMİNE DÖNÜŞTÜREN REDAKSİYON ODASI</div>
    </div>
    <div class="stamp">EDİTÖR ONAYLI • TDK UYUMLU</div>
  </div>
  <div class="main-stage">
    <div class="paper-col">
      <div class="col-head"><span style="color:#DC2626;">KUSURLU METİN (YAPAY ZEKA)</span><span>DÜZELTME ÖNCESİ</span></div>
      <div class="strike-box">
        "Şirketimiz <span class="del">kapsamında</span> önemli bir adım <span class="del">atmaktadır</span> ve <span class="del">süreçlerin yürütülmesine katkı sağlamaktadır</span>. <span class="del">Sonuç olarak</span> bu <span class="del">büyük önem taşımaktadır</span>."
      </div>
      <ul class="notes">
        <li><span style="color:#DC2626;">✍</span> Kırmızı kalemle çizilen kof yardımcı fiiller ve bürokratik laf kalabalığı.</li>
        <li><span style="color:#DC2626;">✍</span> Okuru sıkan mekanik <em>"-mektedir"</em> monotonluğu.</li>
        <li><span style="color:#DC2626;">✍</span> İngilizce kalıbı taklit eden arkadan dolambaçlı yan cümleler.</li>
      </ul>
    </div>
    <div class="paper-col" style="border-top: 4px solid #059669;">
      <div class="col-head"><span style="color:#059669;">ONARILMIŞ METİN (CÜMLE MÜHENDİSİ)</span><span>YAYINA HAZIR</span></div>
      <div class="clean-box">
        "Şirket içi dijital altyapımızı buluta taşıyarak günlük işlerimizi çok daha hızlı ve pürüzsüz yürütmeye başladık."
      </div>
      <ul class="notes">
        <li><span style="color:#059669;">✓</span> Cümle iskeleti öz Türkçe mantığıyla doğrudan hedefe bağlandı.</li>
        <li><span style="color:#059669;">✓</span> Ulaçlarla sağlanan doğal konuşma akıcılığı ve nefes payı.</li>
        <li><span style="color:#059669;">✓</span> %54 kelime tasarrufu ile berrak ve vurucu anlatım.</li>
      </ul>
    </div>
  </div>
  <div class="footer">
    <div>AÇIK KAYNAKLI DİL MİMARİSİ • YEREL VE GİZLİ • MIT LİSANSI</div>
    <div style="font-weight:700; color:#1C1917;">github.com/sahaptanrikulu/cumle-muhendisi</div>
  </div>
</body></html>"""
}

# ------------------------------------------------------------------------------
# 3. Glassmorphism & Mesh Gradient (Apple Vision / Spatial)
# ------------------------------------------------------------------------------
variants[3] = {
    "title": "Glassmorphism & Mesh (Spatial UI)",
    "html": """<!DOCTYPE html>
<html lang="tr"><head><meta charset="UTF-8">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    width: 1600px; height: 900px; background: #0A0A14;
    background-image: 
      radial-gradient(circle at 20% 20%, rgba(99, 102, 241, 0.25) 0%, transparent 50%),
      radial-gradient(circle at 80% 30%, rgba(236, 72, 153, 0.2) 0%, transparent 50%),
      radial-gradient(circle at 50% 80%, rgba(16, 185, 129, 0.2) 0%, transparent 50%);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    color: #FFFFFF; padding: 48px 64px; display: flex; flex-direction: column; justify-content: space-between;
  }
  .header { display: flex; justify-content: space-between; align-items: center; }
  .logo-pill { background: rgba(255,255,255,0.08); backdrop-filter: blur(24px); border: 1px solid rgba(255,255,255,0.15); padding: 10px 24px; border-radius: 9999px; display: flex; align-items: center; gap: 12px; font-weight: 800; font-size: 20px; }
  .stage { display: grid; grid-template-columns: 1fr 1fr; gap: 32px; margin: 24px 0; }
  .glass {
    background: rgba(255, 255, 255, 0.04); backdrop-filter: blur(30px);
    border: 1px solid rgba(255, 255, 255, 0.12); border-radius: 24px; padding: 32px;
    box-shadow: 0 20px 50px rgba(0,0,0,0.3);
  }
  .glass-red { border-color: rgba(244, 63, 94, 0.35); box-shadow: 0 10px 40px rgba(244,63,94,0.12); }
  .glass-green { border-color: rgba(52, 211, 153, 0.4); box-shadow: 0 10px 40px rgba(52,211,153,0.15); }
  .tag { font-size: 12px; font-weight: 800; padding: 6px 14px; border-radius: 9999px; display: inline-block; margin-bottom: 18px; letter-spacing: 0.5px; }
  .tag-r { background: rgba(244, 63, 94, 0.2); color: #FDA4AF; border: 1px solid rgba(244,63,94,0.3); }
  .tag-g { background: rgba(52, 211, 153, 0.2); color: #A7F3D0; border: 1px solid rgba(52,211,153,0.3); }
  .quote { background: rgba(0,0,0,0.3); border-radius: 14px; padding: 18px; font-size: 15px; line-height: 1.55; margin-bottom: 20px; }
  .points { display: flex; flex-direction: column; gap: 10px; font-size: 14.5px; color: #CBD5E1; }
  .footer { display: flex; justify-content: space-between; align-items: center; color: #94A3B8; font-size: 14px; }
</style>
</head><body>
  <div class="header">
    <div class="logo-pill">✨ CÜMLE MÜHENDİSİ <span>v2.0</span></div>
    <div style="font-size:14px; color:#94A3B8; font-weight:600;">DOĞAL TÜRKÇE SENTAKS & RİTİM MOTORU</div>
  </div>
  <div class="stage">
    <div class="glass glass-red">
      <div class="tag tag-r">ÖNCE • ROBOTİK ÇIKTI</div>
      <div class="quote" style="border-left: 3px solid #F43F5E; color:#FECDD3;">
        "Şirketimiz dijital dönüşüm kapsamında önemli bir adım atmaktadır ve bulut altyapımızın kurulması süreçlerin yürütülmesine katkı sağlamaktadır..."
      </div>
      <div class="points">
        <div>✕ 15-20 kelimelik mekanik ve tekdüze cümle ritmi</div>
        <div>✕ İngilizceden miras kalan dolambaçlı yan cümle kopyası</div>
        <div>✕ Kof yardımcı fiiller ve bürokratik laf kalabalığı</div>
        <div>✕ Sonu gelmeyen -mektedir / -maktadır monotonluğu</div>
      </div>
    </div>
    <div class="glass glass-green">
      <div class="tag tag-g">SONRA • İNSAN DİLİYLE YENİDEN İNŞA</div>
      <div class="quote" style="border-left: 3px solid #10B981; color:#D1FAE5; font-weight:600;">
        "Şirket içi dijital altyapımızı buluta taşıyarak günlük işlerimizi çok daha hızlı ve pürüzsüz yürütmeye başladık."
      </div>
      <div class="points">
        <div>✓ Canlı dalgalanan insan ritmi (kısa ve akıcı cümle dengesi)</div>
        <div>✓ Doğrudan hedefe giden sola dallı öz Türkçe mimarisi</div>
        <div>✓ Güçlü ve aktif eylemlerle temizlenmiş berrak anlatım</div>
        <div>✓ Olgusal sadakat: Gerçek verileri ve teknik terimleri koruma</div>
      </div>
    </div>
  </div>
  <div class="footer">
    <div>Açık Kaynak Kodlu • Yerel ve Güvenli Mimari</div>
    <div style="background:rgba(255,255,255,0.08); padding:8px 18px; border-radius:9999px; color:#F8FAFC; font-weight:600;">github.com/sahaptanrikulu/cumle-muhendisi</div>
  </div>
</body></html>"""
}

# ------------------------------------------------------------------------------
# 4. Modern Bento Analytics Dashboard (Metrikler & Dalga Formu)
# ------------------------------------------------------------------------------
variants[4] = {
    "title": "Bento Analytics Dashboard (Metrikler & Ritim)",
    "html": """<!DOCTYPE html>
<html lang="tr"><head><meta charset="UTF-8">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    width: 1600px; height: 900px; background: #0F172A;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    color: #F8FAFC; padding: 44px 60px; display: flex; flex-direction: column; justify-content: space-between;
  }
  .header { display: flex; justify-content: space-between; align-items: center; }
  .h1 { font-size: 28px; font-weight: 800; display: flex; align-items: center; gap: 12px; }
  .bento-grid { display: grid; grid-template-columns: 2fr 1fr; grid-template-rows: auto auto; gap: 20px; margin: 20px 0; }
  .b-box { background: #1E293B; border: 1px solid #334155; border-radius: 16px; padding: 24px; }
  .metric-row { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
  .m-card { background: #0F172A; border: 1px solid #334155; border-radius: 12px; padding: 18px; }
  .m-val { font-size: 38px; font-weight: 900; color: #10B981; line-height: 1; margin: 8px 0; }
  .m-lbl { font-size: 13px; color: #94A3B8; font-weight: 600; text-transform: uppercase; }
  .waveform { width: 100%; height: 70px; margin-top: 10px; }
  .diff-split { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 14px; }
  .diff-box { background: #0F172A; border-radius: 10px; padding: 16px; font-size: 14px; line-height: 1.5; }
  .footer { display: flex; justify-content: space-between; align-items: center; color: #64748B; font-size: 13.5px; }
</style>
</head><body>
  <div class="header">
    <div class="h1"><span style="color:#38BDF8;">📐</span> CÜMLE MÜHENDİSİ ANALİTİK PANELİ</div>
    <div style="background:#1E293B; border:1px solid #334155; padding:6px 16px; border-radius:8px; font-size:13px; color:#94A3B8;">CANLI SENTAKS VE RİTİM DENETLEYİCİSİ</div>
  </div>
  <div class="bento-grid">
    <div class="b-box" style="grid-row: span 2;">
      <div style="font-size:13px; font-weight:800; color:#38BDF8; letter-spacing:1px; margin-bottom:12px;">CANLI DİFF VE CÜMLE DÖNÜŞÜMÜ</div>
      <div class="diff-split">
        <div class="diff-box" style="border:1px solid rgba(239,68,68,0.4);">
          <div style="color:#EF4444; font-weight:800; font-size:12px; margin-bottom:6px;">ÖNCE (ROBOTİK KALIP)</div>
          <p style="color:#94A3B8;">"Şirketimiz dijital dönüşüm kapsamında önemli bir adım atmaktadır ve bulut altyapımızın kurulması süreçlerin yürütülmesine katkı sağlamaktadır..."</p>
          <div style="margin-top:14px; font-size:12px; color:#F87171;">✕ CoV: 0.12 (Monoton) • %100 -mektedir</div>
        </div>
        <div class="diff-box" style="border:1px solid rgba(16,185,129,0.5); background:#064E3B20;">
          <div style="color:#10B981; font-weight:800; font-size:12px; margin-bottom:6px;">SONRA (ONARILMIŞ İNSAN DİLİ)</div>
          <p style="color:#F1F5F9; font-weight:550;">"Şirket içi dijital altyapımızı buluta taşıyarak günlük işlerimizi çok daha hızlı ve pürüzsüz yürütmeye başladık."</p>
          <div style="margin-top:14px; font-size:12px; color:#34D399;">✓ CoV: 0.58 (Canlı İnsan Ritmi) • %0 Kof Fiil</div>
        </div>
      </div>
      <div style="margin-top:20px; font-size:13px; font-weight:700; color:#94A3B8;">CÜMLE UZUNLUĞU VE RİTİM DALGASI (BURSTINESS COV)</div>
      <svg class="waveform" viewBox="0 0 800 70">
        <!-- Flat robot line -->
        <path d="M 0 50 Q 200 48, 400 50 T 800 50" fill="none" stroke="#EF4444" stroke-width="2" stroke-dasharray="4"/>
        <!-- Dynamic human wave -->
        <path d="M 0 50 Q 100 10, 200 45 T 400 20 T 600 55 T 800 25" fill="none" stroke="#10B981" stroke-width="3"/>
      </svg>
      <div style="display:flex; justify-content:space-between; font-size:11.5px; color:#64748B; margin-top:4px;">
        <span style="color:#EF4444;">-- Yapay Zeka: Düz, sığ ve tekdüze (CoV &lt; 0.30)</span>
        <span style="color:#10B981;">━ Cümle Mühendisi: Canlı, nefes alan dalga (CoV &gt; 0.40)</span>
      </div>
    </div>
    <div class="b-box">
      <div class="metric-row">
        <div class="m-card">
          <div class="m-lbl">Ritim Çeşitliliği</div>
          <div class="m-val">0.58</div>
          <div style="font-size:12px; color:#10B981;">✓ Hedef CoV &ge; 0.40</div>
        </div>
        <div class="m-card">
          <div class="m-lbl">Kelime Tasarrufu</div>
          <div class="m-val">%54</div>
          <div style="font-size:12px; color:#38BDF8;">Boş fiil tasfiyesi</div>
        </div>
      </div>
    </div>
    <div class="b-box">
      <div style="font-size:13px; font-weight:700; color:#38BDF8; margin-bottom:8px;">MİMARİ TEST ÇEKİRDEĞİ</div>
      <div style="font-size:13px; color:#94A3B8; line-height:1.5;">
        • TDK Tipografi & Saat/Yüzde Standartları<br>
        • Olgusal Sadakat Kilidi (Sıfır Uydurma)<br>
        • SDI / NFPA / fire-rated Terim Kalkanı
      </div>
    </div>
  </div>
  <div class="footer">
    <div>%100 AÇIK KAYNAK • DETERMINISTIC PYTHON CLI TEST MOTORU</div>
    <div style="color:#F8FAFC; font-weight:600;">github.com/sahaptanrikulu/cumle-muhendisi</div>
  </div>
</body></html>"""
}

# ------------------------------------------------------------------------------
# 5. Split-Screen Dual Tone (Dramatik Gece / Gündüz Kırılması)
# ------------------------------------------------------------------------------
variants[5] = {
    "title": "Split-Screen Dual Tone (Gece & Gündüz)",
    "html": """<!DOCTYPE html>
<html lang="tr"><head><meta charset="UTF-8">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    width: 1600px; height: 900px; display: flex; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  }
  .side { width: 50%; height: 100%; padding: 60px; display: flex; flex-direction: column; justify-content: space-between; position: relative; }
  .side-left { background: #111827; color: #F8FAFC; border-right: 2px solid #DC2626; }
  .side-right { background: #042F2E; color: #F0FDF4; }
  .badge { font-size: 13px; font-weight: 800; padding: 6px 14px; border-radius: 6px; display: inline-block; text-transform: uppercase; }
  .badge-l { background: rgba(220, 38, 38, 0.2); color: #F87171; border: 1px solid rgba(220,38,38,0.4); }
  .badge-r { background: rgba(16, 185, 129, 0.2); color: #34D399; border: 1px solid rgba(16,185,129,0.4); }
  .big-text { font-size: 40px; font-weight: 900; margin: 20px 0 10px; line-height: 1.1; }
  .sample { background: rgba(0,0,0,0.3); border-radius: 12px; padding: 22px; font-size: 16px; line-height: 1.6; margin: 20px 0; }
  .list { display: flex; flex-direction: column; gap: 12px; font-size: 15.5px; }
  .divider-laser { position: absolute; right: -15px; top: 50%; transform: translateY(-50%); width: 30px; height: 60px; background: #000; border: 2px solid #38BDF8; border-radius: 9999px; display: flex; align-items: center; justify-content: center; font-weight: 900; color: #38BDF8; z-index: 10; box-shadow: 0 0 20px #38BDF8; }
</style>
</head><body>
  <div class="side side-left">
    <div class="divider-laser">➔</div>
    <div>
      <div class="badge badge-l">YAPAY ZEKA SOĞUKLUĞU</div>
      <div class="big-text" style="color:#FCA5A5;">Kalıpların Esiri.</div>
      <p style="color:#94A3B8; font-size:15px;">Mekanik, tekdüze ve çeviri kokan satırlar.</p>
    </div>
    <div class="sample" style="border-left:4px solid #EF4444; color:#FCA5A5;">
      "Şirketimiz dijital dönüşüm kapsamında önemli bir adım atmaktadır ve bulut altyapımızın kurulması süreçlerin yürütülmesine katkı sağlamaktadır..."
    </div>
    <div class="list" style="color:#94A3B8;">
      <div>✕ 15-20 kelimelik mekanik cümle hapishanesi</div>
      <div>✕ İngilizce düşünülüp arkadan dolandırılan anlatım</div>
      <div>✕ Kof yardımcı fiillerle şişirilmiş memur dili</div>
      <div>✕ Sonu gelmeyen -mektedir / -maktadır tekdüzeliği</div>
    </div>
    <div style="font-size:13px; color:#64748B;">HANTAL VE ROBOTİK ÇIKTI</div>
  </div>
  <div class="side side-right">
    <div>
      <div class="badge badge-r">CÜMLE MÜHENDİSİ DOKUNUŞU</div>
      <div class="big-text" style="color:#6EE7B7;">Özgür & Yaşayan Dil.</div>
      <p style="color:#A7F3D0; font-size:15px;">Öz Türkçe mimarisi ve canlı insan ritmi.</p>
    </div>
    <div class="sample" style="border-left:4px solid #10B981; color:#D1FAE5; font-weight:600;">
      "Şirket içi dijital altyapımızı buluta taşıyarak günlük işlerimizi çok daha hızlı ve pürüzsüz yürütmeye başladık."
    </div>
    <div class="list" style="color:#A7F3D0;">
      <div>✓ Kısa hüküm cümleleri ve ulaçlı akıcı uzunluk dengesi</div>
      <div>✓ Doğrudan hedefe bağlanan sola dallı Türkçe sentaksı</div>
      <div>✓ Fazlalıklardan arınmış aktif ve güçlü eylemler</div>
      <div>✓ Olgusal sadakat: Gerçek verileri ve teknik terimleri koruma</div>
    </div>
    <div style="display:flex; justify-content:space-between; align-items:center; font-size:13px; color:#6EE7B7; font-weight:700;">
      <span>github.com/sahaptanrikulu/cumle-muhendisi</span>
      <span>v2.0 AÇIK KAYNAK</span>
    </div>
  </div>
</body></html>"""
}

# ------------------------------------------------------------------------------
# 6. Architectural Blueprint (Teknik Çizim Masası)
# ------------------------------------------------------------------------------
variants[6] = {
    "title": "Architectural Blueprint (Mavi Pafta)",
    "html": """<!DOCTYPE html>
<html lang="tr"><head><meta charset="UTF-8">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    width: 1600px; height: 900px; background: #0A192F;
    background-image: 
      linear-gradient(rgba(56, 189, 248, 0.1) 1px, transparent 1px),
      linear-gradient(90deg, rgba(56, 189, 248, 0.1) 1px, transparent 1px),
      linear-gradient(rgba(56, 189, 248, 0.03) 10px, transparent 10px),
      linear-gradient(90deg, rgba(56, 189, 248, 0.03) 10px, transparent 10px);
    background-size: 100px 100px, 100px 100px, 20px 20px, 20px 20px;
    font-family: ui-monospace, "SF Mono", "Segoe UI Mono", monospace;
    color: #E2E8F0; padding: 48px 64px; display: flex; flex-direction: column; justify-content: space-between;
  }
  .header { border-bottom: 2px solid #38BDF8; padding-bottom: 20px; display: flex; justify-content: space-between; align-items: flex-end; }
  .title { font-size: 36px; font-weight: 900; color: #38BDF8; letter-spacing: 2px; }
  .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 32px; margin: 24px 0; }
  .schematic-box { border: 1.5px dashed #38BDF8; border-radius: 8px; padding: 26px; background: rgba(10, 25, 47, 0.7); position: relative; }
  .dim-line { border-top: 1px dashed #38BDF8; margin: 15px 0; text-align: center; font-size: 12px; color: #38BDF8; position: relative; }
  .dim-line span { background: #0A192F; padding: 0 10px; position: relative; top: -9px; }
  .sample { background: rgba(0,0,0,0.5); border: 1px solid rgba(56,189,248,0.3); border-radius: 6px; padding: 18px; font-size: 14.5px; line-height: 1.6; }
  .rules { margin-top: 16px; font-size: 13.5px; line-height: 1.6; color: #94A3B8; }
  .footer { border-top: 2px solid #38BDF8; padding-top: 18px; display: flex; justify-content: space-between; font-size: 13px; color: #38BDF8; }
</style>
</head><body>
  <div class="header">
    <div>
      <div class="title">📐 CÜMLE MÜHENDİSİ // DİL ŞARTNAMESİ</div>
      <div style="font-size:13px; color:#94A3B8; margin-top:4px;">PROJE KODU: CM-TR-V2 • MİMARİ SENTAKS PROTOKOLÜ</div>
    </div>
    <div style="border:1px solid #38BDF8; padding:6px 14px; font-size:12px; color:#38BDF8;">TOLERANS: 0 AI HATASI</div>
  </div>
  <div class="grid">
    <div class="schematic-box" style="border-color:#EF4444;">
      <div style="color:#EF4444; font-weight:800; font-size:13px; margin-bottom:10px;">[ŞEMA A] STATİK HATALI YAPI (ROBOTİK)</div>
      <div class="sample" style="color:#FCA5A5;">
        "Şirketimiz dijital dönüşüm kapsamında önemli bir adım atmaktadır ve bulut altyapımızın kurulması süreçlerin yürütülmesine katkı sağlamaktadır..."
      </div>
      <div class="dim-line"><span>▲ 16 KELİME • AŞIRI YÜKLEME ▲</span></div>
      <div class="rules">
        - HATA 01: Saatin tiktakı gibi 15-20 kelimelik mekanik mimari<br>
        - HATA 02: İngilizce SVO taklidi, arkadan dolanan yan cümleler<br>
        - HATA 03: Kof taşıyıcı fiiller ("gerçekleştirmek", "sağlamak")<br>
        - HATA 04: Sonu gelmeyen -mektedir / -maktadır korozyonu
      </div>
    </div>
    <div class="schematic-box" style="border-color:#10B981;">
      <div style="color:#10B981; font-weight:800; font-size:13px; margin-bottom:10px;">[ŞEMA B] MÜHENDİSLİK MONTAJI (ÖZ TÜRKÇE)</div>
      <div class="sample" style="color:#6EE7B7; border-color:#10B981;">
        "Şirket içi dijital altyapımızı buluta taşıyarak günlük işlerimizi çok daha hızlı ve pürüzsüz yürütmeye başladık."
      </div>
      <div class="dim-line" style="border-color:#10B981;"><span style="color:#10B981;">▼ %54 KELİME TASARRUFU • MAKSİMUM DAYANIM ▼</span></div>
      <div class="rules" style="color:#A7F3D0;">
        + ÇÖZÜM 01: Sola dallanma sentaksı (sıfat-fiille doğrudan bağlama)<br>
        + ÇÖZÜM 02: Ulaç sistemiyle birbirine kenetlenen akıcı eylemler<br>
        + ÇÖZÜM 03: Güçlü ve aktif yüklemlerle kurulan sağlam omurga<br>
        + ÇÖZÜM 04: Sektörel terim sadakati (SDI, NFPA, fire-rated)
      </div>
    </div>
  </div>
  <div class="footer">
    <div>ÇEKİRDEK: PYTHON DETERMINISTIC CLI ENGINE • MIT LİSANSI</div>
    <div>REPO: github.com/sahaptanrikulu/cumle-muhendisi</div>
  </div>
</body></html>"""
}

# ------------------------------------------------------------------------------
# 7. Retro Hacker CRT Terminal (Monospace HUD)
# ------------------------------------------------------------------------------
variants[7] = {
    "title": "Retro Hacker Terminal (Cyberpunk HUD)",
    "html": """<!DOCTYPE html>
<html lang="tr"><head><meta charset="UTF-8">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    width: 1600px; height: 900px; background: #050505;
    background-image: linear-gradient(rgba(0, 255, 102, 0.03) 1px, transparent 1px);
    background-size: 100% 4px;
    font-family: ui-monospace, "Courier New", monospace;
    color: #00FF66; padding: 48px 64px; display: flex; flex-direction: column; justify-content: space-between;
  }
  .top { border-bottom: 1px solid #00FF66; padding-bottom: 16px; display: flex; justify-content: space-between; }
  .term-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin: 24px 0; }
  .term-box { border: 1px solid rgba(0,255,102,0.4); background: rgba(0,20,0,0.6); border-radius: 8px; padding: 24px; box-shadow: 0 0 20px rgba(0,255,102,0.1); }
  .cmd { color: #FFFFFF; font-weight: bold; margin-bottom: 14px; }
  .output { line-height: 1.6; font-size: 14.5px; }
  .footer { border-top: 1px solid #00FF66; padding-top: 16px; display: flex; justify-content: space-between; font-size: 13.5px; }
</style>
</head><body>
  <div class="top">
    <div>>>> CUMLE_MUHENDISI_CLI v2.0 // STATUS: ONLINE</div>
    <div>SYS_LANG: TR-TR • AST_PARSER: ACTIVE</div>
  </div>
  <div class="term-grid">
    <div class="term-box" style="border-color:#FF3366; color:#FF3366;">
      <div class="cmd">$ cumle-muhendisi audit --target=raw_ai.md</div>
      <div class="output">
        [FAIL] 4 CRITICAL VIOLATIONS DETECTED:<br><br>
        > "Şirketimiz dijital dönüşüm kapsamında önemli bir adım atmaktadır ve bulut altyapımızın kurulması süreçlerin yürütülmesine katkı sağlamaktadır..."<br><br>
        - [P0] Light-Verb Inflation: "katkı sağlamak"<br>
        - [P0] Monotonous Suffix: 100% "-mektedir"<br>
        - [P1] English Calque: Right-Branching Subclause<br>
        - [P2] Rhythm CoV: 0.14 (Machine Metronome Alarm)
      </div>
    </div>
    <div class="term-box" style="border-color:#00FF66; color:#00FF66;">
      <div class="cmd">$ cumle-muhendisi rebuild --stream --clean</div>
      <div class="output">
        [SUCCESS] REBUILT TO NATURAL TURKISH SYNTAX:<br><br>
        > "Şirket içi dijital altyapımızı buluta taşıyarak günlük işlerimizi çok daha hızlı ve pürüzsüz yürütmeye başladık."<br><br>
        + [PASS] Sola Dallanma Sentaksı Uygulandı<br>
        + [PASS] Ulaç Sistemiyle Akıcılık Sağlandı<br>
        + [PASS] Burstiness CoV: 0.58 (Canlı İnsan Ritmi)<br>
        + [PASS] Olgusal Sadakat: Sıfır Halüsinasyon
      </div>
    </div>
  </div>
  <div class="footer">
    <div>ROOT ACCESS: LOCAL ONLY • ZERO TELEMETRY • MIT LICENSE</div>
    <div>git clone https://github.com/sahaptanrikulu/cumle-muhendisi</div>
  </div>
</body></html>"""
}

# ------------------------------------------------------------------------------
# 8. Swiss Modernism / Bauhaus Typographic
# ------------------------------------------------------------------------------
variants[8] = {
    "title": "Swiss Modernism / Bauhaus (İsviçre Tipografisi)",
    "html": """<!DOCTYPE html>
<html lang="tr"><head><meta charset="UTF-8">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    width: 1600px; height: 900px; background: #F4F4F0;
    font-family: -apple-system, "Helvetica Neue", Arial, sans-serif;
    color: #000000; padding: 50px 70px; display: flex; flex-direction: column; justify-content: space-between;
  }
  .h1 { font-size: 64px; font-weight: 900; letter-spacing: -2px; line-height: 0.95; text-transform: uppercase; }
  .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 36px; margin: 28px 0; }
  .block { border: 4px solid #000000; padding: 32px; background: #FFFFFF; }
  .block-accent { background: #0038FF; color: #FFFFFF; border-color: #0038FF; }
  .num { font-size: 32px; font-weight: 900; margin-bottom: 12px; }
  .text-box { font-size: 18px; line-height: 1.5; font-weight: 600; margin-bottom: 20px; }
  .footer { border-top: 4px solid #000000; padding-top: 20px; display: flex; justify-content: space-between; font-weight: 800; font-size: 15px; text-transform: uppercase; }
</style>
</head><body>
  <div style="display:flex; justify-content:space-between; align-items:flex-start;">
    <div class="h1">CÜMLE<br>MÜHENDİSİ.</div>
    <div style="font-size:16px; font-weight:800; text-align:right; max-width:400px; line-height:1.4;">
      TÜRKÇE İÇİN MİMARİ REDAKSİYON SİSTEMİ. YAPAY ZEKA SOĞUKLUĞUNA SON.
    </div>
  </div>
  <div class="grid">
    <div class="block">
      <div class="num" style="color:#DC2626;">01 / REDDEDİLEN</div>
      <div class="text-box" style="color:#78716C;">
        "Şirketimiz dijital dönüşüm kapsamında önemli bir adım atmaktadır ve bulut altyapımızın kurulması süreçlerin yürütülmesine katkı sağlamaktadır..."
      </div>
      <div style="font-size:14.5px; line-height:1.6; font-weight:700;">
        ✕ Saatin tiktakı gibi 15-20 kelimelik tekdüzelik<br>
        ✕ İngilizceden miras kalan dolambaçlı yan cümleler<br>
        ✕ Kof fiil şişkinliği ve -mektedir monotonluğu
      </div>
    </div>
    <div class="block block-accent">
      <div class="num" style="color:#FFFFFF;">02 / İNŞA EDİLEN</div>
      <div class="text-box" style="color:#FFFFFF;">
        "Şirket içi dijital altyapımızı buluta taşıyarak günlük işlerimizi çok daha hızlı ve pürüzsüz yürütmeye başladık."
      </div>
      <div style="font-size:14.5px; line-height:1.6; font-weight:500; opacity:0.9;">
        ✓ Öz Türkçe sola dallanma sentaksı<br>
        ✓ Ulaçlarla kurulan dinamik insan ritmi<br>
        ✓ %54 kelime tasarrufu ile berrak güç
      </div>
    </div>
  </div>
  <div class="footer">
    <div>V2.0 • %100 AÇIK KAYNAK • MIT LİSANSI</div>
    <div>GITHUB.COM/SAHAPTANRIKULU/CUMLE-MUHENDISI</div>
  </div>
</body></html>"""
}

# ------------------------------------------------------------------------------
# 9. Modern IDE Code Diff View (VS Code / Cursor Studio)
# ------------------------------------------------------------------------------
variants[9] = {
    "title": "Modern IDE Diff View (VS Code / Cursor Studio)",
    "html": """<!DOCTYPE html>
<html lang="tr"><head><meta charset="UTF-8">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    width: 1600px; height: 900px; background: #181824;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    color: #F8FAFC; padding: 40px 60px; display: flex; flex-direction: column; justify-content: space-between;
  }
  .ide-window {
    background: #1E1E2E; border: 1px solid #313244; border-radius: 16px;
    box-shadow: 0 25px 60px rgba(0,0,0,0.5); overflow: hidden; display: flex; flex-direction: column; flex: 1; margin: 15px 0;
  }
  .title-bar { background: #181825; padding: 12px 18px; display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid #313244; }
  .dots { display: flex; gap: 8px; }
  .dot { width: 12px; height: 12px; border-radius: 50%; }
  .tabs { display: flex; background: #181825; border-bottom: 1px solid #313244; }
  .tab { padding: 10px 22px; font-size: 13.5px; font-family: monospace; border-right: 1px solid #313244; color: #A6ADC8; }
  .tab.active { background: #1E1E2E; color: #CDD6F4; border-top: 2px solid #89B4FA; }
  .editor-body { display: grid; grid-template-columns: 1fr 1fr; flex: 1; font-family: ui-monospace, monospace; font-size: 15px; }
  .pane { padding: 24px; line-height: 1.7; }
  .pane-left { border-right: 1px solid #313244; background: rgba(243, 139, 168, 0.05); }
  .pane-right { background: rgba(166, 227, 161, 0.05); }
  .diff-del { background: rgba(243, 139, 168, 0.2); color: #F38BA8; padding: 2px 6px; border-radius: 4px; }
  .diff-add { background: rgba(166, 227, 161, 0.2); color: #A6E3A1; padding: 2px 6px; border-radius: 4px; font-weight: bold; }
  .terminal-drawer { background: #11111B; border-top: 1px solid #313244; padding: 12px 20px; font-family: monospace; font-size: 13px; color: #A6ADC8; display: flex; justify-content: space-between; }
</style>
</head><body>
  <div style="display:flex; justify-content:space-between; align-items:center;">
    <div style="font-size:26px; font-weight:800; display:flex; align-items:center; gap:10px;">
      💻 CÜMLE MÜHENDİSİ // IDE DİFF GÖRÜNÜMÜ
    </div>
    <div style="color:#89B4FA; font-weight:600; font-size:14px;">AST PARSER & LINGUISTIC REFACTOR ENGINE</div>
  </div>
  <div class="ide-window">
    <div class="title-bar">
      <div class="dots">
        <div class="dot" style="background:#F38BA8;"></div>
        <div class="dot" style="background:#F9E2AF;"></div>
        <div class="dot" style="background:#A6E3A1;"></div>
      </div>
      <div style="font-size:13px; color:#6C7086; font-family:monospace;">cumle-muhendisi — git diff HEAD~1</div>
      <div></div>
    </div>
    <div class="tabs">
      <div class="tab">metin_ham_ai.md</div>
      <div class="tab active">metin_cumle_muhendisi.md (Onarılmış)</div>
    </div>
    <div class="editor-body">
      <div class="pane pane-left">
        <div style="color:#F38BA8; font-weight:bold; margin-bottom:12px;">// ÖNCE: ROBOTİK SÖZ DİZİMİ</div>
        <p>1 | <span class="diff-del">- "Şirketimiz dijital dönüşüm kapsamında</span></p>
        <p>2 | <span class="diff-del">- önemli bir adım atmaktadır</span></p>
        <p>3 | <span class="diff-del">- ve bulut altyapımızın kurulması</span></p>
        <p>4 | <span class="diff-del">- süreçlerin yürütülmesine katkı sağlamaktadır..."</span></p>
        <br>
        <p style="color:#6C7086; font-size:13px;">// Kusurlar: 4x Kof Fiil • -mektedir Monotonluğu • Sağa Dallı Sentaks</p>
      </div>
      <div class="pane pane-right">
        <div style="color:#A6E3A1; font-weight:bold; margin-bottom:12px;">// SONRA: ÖZ TÜRKÇE MİMARİSİ</div>
        <p>1 | <span class="diff-add">+ "Şirket içi dijital altyapımızı buluta taşıyarak</span></p>
        <p>2 | <span class="diff-add">+ günlük işlerimizi çok daha hızlı</span></p>
        <p>3 | <span class="diff-add">+ ve pürüzsüz yürütmeye başladık."</span></p>
        <br><br>
        <p style="color:#A6E3A1; font-size:13px;">// Çözüm: Ulaçlı Bağlama • Güçlü Eylem • CoV 0.58 Canlı Ritim</p>
      </div>
    </div>
    <div class="terminal-drawer">
      <div>✔ 0 AI/TDK Sinyali • Burstiness CoV: 0.58 (İnsan Seviyesi) • %54 Kelime Tasarrufu</div>
      <div style="color:#89B4FA;">Tests Passed: 100%</div>
    </div>
  </div>
  <div style="display:flex; justify-content:space-between; color:#6C7086; font-size:13.5px;">
    <div>⚡ %100 Açık Kaynak • CLI & Skill Desteği</div>
    <div style="color:#CDD6F4; font-weight:600;">github.com/sahaptanrikulu/cumle-muhendisi</div>
  </div>
</body></html>"""
}

# ------------------------------------------------------------------------------
# 10. 3D Isometric Studio Poster (Lansman Afişi / Derinlikli Sinematik)
# ------------------------------------------------------------------------------
variants[10] = {
    "title": "3D Isometric Studio Poster (Lansman Afişi)",
    "html": """<!DOCTYPE html>
<html lang="tr"><head><meta charset="UTF-8">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    width: 1600px; height: 900px; background: #090D16;
    background-image: 
      radial-gradient(circle at 50% 10%, rgba(37, 99, 235, 0.25) 0%, transparent 60%),
      radial-gradient(circle at 10% 90%, rgba(16, 185, 129, 0.15) 0%, transparent 50%),
      radial-gradient(circle at 90% 90%, rgba(244, 63, 94, 0.15) 0%, transparent 50%);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    color: #F8FAFC; padding: 48px 64px; display: flex; flex-direction: column; justify-content: space-between;
  }
  .hero-tag { font-size: 13px; font-weight: 800; color: #38BDF8; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 8px; }
  .hero-title { font-size: 48px; font-weight: 900; letter-spacing: -1px; }
  .stage-3d { display: grid; grid-template-columns: 1fr 1fr; gap: 40px; margin: 30px 0; perspective: 1000px; }
  .box-3d {
    background: linear-gradient(145deg, rgba(30, 41, 59, 0.8), rgba(15, 23, 42, 0.9));
    border: 1.5px solid rgba(255, 255, 255, 0.12); border-radius: 24px; padding: 36px;
    box-shadow: 0 30px 60px rgba(0,0,0,0.4), inset 0 1px 0 rgba(255,255,255,0.1);
  }
  .box-3d-left { border-color: rgba(239, 68, 68, 0.4); box-shadow: -10px 20px 50px rgba(239,68,68,0.15); }
  .box-3d-right { border-color: rgba(16, 185, 129, 0.45); box-shadow: 10px 20px 50px rgba(16,185,129,0.2); }
  .pill-3d { padding: 6px 16px; border-radius: 9999px; font-size: 12px; font-weight: 800; display: inline-block; margin-bottom: 18px; }
  .sample-quote { background: rgba(0,0,0,0.4); border-radius: 14px; padding: 20px; font-size: 16px; line-height: 1.6; margin-bottom: 22px; }
  .footer { display: flex; justify-content: space-between; align-items: center; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 20px; color: #64748B; font-size: 14px; }
</style>
</head><body>
  <div style="text-align:center;">
    <div class="hero-tag">TÜRKÇE İÇİN AÇIK KAYNAK DİL MİMARİSİ</div>
    <div class="hero-title">CÜMLE MÜHENDİSİ</div>
  </div>
  <div class="stage-3d">
    <div class="box-3d box-3d-left">
      <div class="pill-3d" style="background:rgba(239,68,68,0.2); color:#FCA5A5; border:1px solid rgba(239,68,68,0.4);">
        ÖNCE • ROBOTİK ÇIKTI
      </div>
      <div class="sample-quote" style="border-left:4px solid #EF4444; color:#FCA5A5;">
        "Şirketimiz dijital dönüşüm kapsamında önemli bir adım atmaktadır ve bulut altyapımızın kurulması süreçlerin yürütülmesine katkı sağlamaktadır..."
      </div>
      <div style="color:#94A3B8; font-size:15px; line-height:1.7;">
        ✕ Saatin tiktakı gibi 15-20 kelimelik tekdüzelik<br>
        ✕ İngilizceden miras kalan dolambaçlı yan cümle kopyası<br>
        ✕ Kof yardımcı fiiller ("gerçekleştirmek", "katkı sağlamak")<br>
        ✕ Sonu gelmeyen -mektedir / -maktadır monotonluğu
      </div>
    </div>
    <div class="box-3d box-3d-right">
      <div class="pill-3d" style="background:rgba(16,185,129,0.2); color:#6EE7B7; border:1px solid rgba(16,185,129,0.4);">
        SONRA • CÜMLE MÜHENDİSİ
      </div>
      <div class="sample-quote" style="border-left:4px solid #10B981; color:#D1FAE5; font-weight:600;">
        "Şirket içi dijital altyapımızı buluta taşıyarak günlük işlerimizi çok daha hızlı ve pürüzsüz yürütmeye başladık."
      </div>
      <div style="color:#A7F3D0; font-size:15px; line-height:1.7;">
        ✓ Canlı dalgalanan insan ritmi (kısa ve akıcı cümle dengesi)<br>
        ✓ Doğrudan hedefe giden sola dallı öz Türkçe mimarisi<br>
        ✓ Güçlü ve aktif eylemlerle temizlenmiş berrak anlatım<br>
        ✓ Olgusal sadakat: Gerçek verileri ve teknik terimleri koruma
      </div>
    </div>
  </div>
  <div class="footer">
    <div>⚡ %100 Açık Kaynak • Yerel Gizlilik • MIT Lisansı</div>
    <div style="color:#F8FAFC; font-weight:700;">github.com/sahaptanrikulu/cumle-muhendisi</div>
  </div>
</body></html>"""
}

# ==============================================================================
# WRITE ALL HTML AND RENDER TO PNG WITH CHROME HEADLESS
# ==============================================================================

print("Generating 10 HTML files and rendering 10 PNG images...")

for num, data in variants.items():
    html_file = os.path.join(variants_dir, f"variant_{num}.html")
    png_file = os.path.join(variants_dir, f"variant_{num}.png")
    
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(data["html"])
        
    cmd = [
        chrome_path,
        "--headless",
        "--disable-gpu",
        f"--screenshot={png_file}",
        "--window-size=1600,900",
        "--hide-scrollbars",
        f"file:///{html_file}"
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    size = os.path.getsize(png_file) if os.path.exists(png_file) else 0
    print(f"Variant {num:2d} ({data['title']}): Rendered -> {size} bytes")

print("All 10 variants successfully rendered!")
