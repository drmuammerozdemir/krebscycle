import streamlit as st
import streamlit.components.v1 as components

# Sayfa Yapılandırması (Geniş Ekran ve Tıbbi Tema)
st.set_page_config(
    page_title="Krebs Siklusu & PDH İnteraktif Öğrenme Platformu",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Streamlit Tema ve Özel CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&family=DM+Sans:wght@400;500;700&family=JetBrains+Mono:wght@600;700&display=swap');
    
    .stApp {
        background-color: #0b1120;
        color: #f8fafc;
        font-family: 'DM Sans', sans-serif;
    }
    
    /* Üst Başlık Banner */
    .top-header {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        border: 1px solid #334155;
        border-radius: 16px;
        padding: 20px 28px;
        margin-bottom: 20px;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.5);
    }
    .top-header h1 {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 26px;
        font-weight: 700;
        color: #f8fafc;
        margin: 0;
        letter-spacing: -0.5px;
    }
    .top-header p {
        color: #38bdf8;
        font-size: 14px;
        margin: 6px 0 0 0;
    }
    .badge-pill {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 9999px;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.8px;
        text-transform: uppercase;
        background-color: rgba(56, 189, 248, 0.15);
        color: #38bdf8;
        border: 1px solid rgba(56, 189, 248, 0.3);
        margin-bottom: 8px;
    }
    
    /* Sidebar stillendirmesi */
    [data-testid="stSidebar"] {
        background-color: #0f172a;
        border-right: 1px solid #1e293b;
    }
</style>
""", unsafe_allow_html=True)

# Üst Bilgi Kartı
st.markdown("""
<div class="top-header">
    <span class="badge-pill">KTO Karatay Tıp Fakültesi • Tıbbi Biyokimya AD</span>
    <h1>Krebs Döngüsü & PDH Çift Yönlü İnteraktif İstasyon</h1>
    <p>Sol taraftaki <strong>Kelime Avı</strong>'nda yatay ve dikey gizlenmiş metabolit ve kofaktörleri seçin; bulduğunuz her terimi sağdaki <strong>PDH & Krebs Siklusu</strong> boşluklarına sürükleyip bırakın.</p>
</div>
""", unsafe_allow_html=True)

# Yan Panel (Sidebar) Kontrolleri
with st.sidebar:
    st.header("🎯 Etkinlik Kontrolü")
    st.markdown("""
    **Ders:** Tıbbi Biyokimya  
    **Konu:** Krebs Döngüsü & PDH Kompleksi  
    **Eğitici:** Dr. Muammer Özdemir (2026-2027)
    """)
    st.divider()
    
    st.subheader("💡 Nasıl Oynanır?")
    st.markdown("""
    1. **Kelimeyi Seçin:**  
       Soldaki harf ızgarasında fareyle sürükleyerek veya telefon/tablette parmağınızla harflerin üzerinden geçerek kelimeleri işaretleyin.
    2. **Şemayı Tamamlayın:**  
       Bulduğunuz kelimeler sağdaki şemada yeşile döner. Kelime kutucuğunu tutup sağdaki doğru biyokimyasal basamağa **sürükleyin** (veya tıklayıp hedef kutuyu seçin).
    3. **Klinik İpuçları:**  
       İnhibitörler (Arsenik, Floroasetat, Malonat) için özel kırmızı hedef alanlarını kullanın.
    """)
    st.divider()

    st.subheader("📚 TUS & Komite İpuçları")
    with st.expander("PDH Kofaktörleri (5 Kofaktör)"):
        st.write("**Tenha Lokantada Köfte, Fasulye, Nohut**")
        st.caption("TPP (B1), Lipoik Asit, KoA (B5), FAD (B2), NAD+ (B3)")
    with st.expander("Siklus Ara Ürünleri"):
        st.write("**Sonunda İki Kardeş (Süksinil & Süksinat) Fırından Malatya Otlu Ekmeği Aldı**")
        st.caption("Sitrat → İzositrat → α-KG → Süksinil-KoA → Süksinat → Fumarat → Malat → Oksaloasetat")
    with st.expander("Klinik Blokajlar"):
        st.write("• **Arsenik:** Lipoik asidin -SH grubunu bağlar.")
        st.write("• **Floroasetat:** Akonitazı bloke eder.")
        st.write("• **Malonat:** Kompleks II'yi kompetitif inhibe eder.")

# HTML5 / JavaScript / CSS Entegre İnteraktif Uygulama Kodu
interactive_app_code = """
<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=Space+Grotesk:wght@600;700&family=JetBrains+Mono:wght@700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
<style>
    * {
        box-sizing: border-box;
        user-select: none;
        -webkit-user-select: none;
    }
    body {
        margin: 0;
        padding: 0;
        background: transparent;
        font-family: 'DM Sans', sans-serif;
        color: #f1f5f9;
        overflow-x: hidden;
    }

    /* İki Sütunlu Ana Grid */
    .app-wrapper {
        display: grid;
        grid-template-columns: 490px 1fr;
        gap: 20px;
        width: 100%;
        min-height: 860px;
    }

    @media (max-width: 1100px) {
        .app-wrapper {
            grid-template-columns: 1fr;
        }
    }

    .panel-card {
        background-color: #0f172a;
        border: 1px solid #1e293b;
        border-radius: 16px;
        padding: 18px;
        box-shadow: 0 12px 30px rgba(0, 0, 0, 0.4);
        display: flex;
        flex-direction: column;
    }

    .panel-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 14px;
        border-bottom: 1px solid #1e293b;
        padding-bottom: 10px;
    }

    .panel-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 18px;
        font-weight: 700;
        color: #38bdf8;
        display: flex;
        align-items: center;
        gap: 8px;
        margin: 0;
    }

    .score-badge {
        background: rgba(56, 189, 248, 0.12);
        color: #38bdf8;
        border: 1px solid rgba(56, 189, 248, 0.3);
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 700;
    }

    /* =========================================================
       SOL TARAF: KELİME AVI (WORD SEARCH GRID)
       ========================================================= */
    .grid-container {
        display: flex;
        justify-content: center;
        align-items: center;
        background-color: #0b1120;
        border: 2px solid #334155;
        border-radius: 12px;
        padding: 8px;
        margin-bottom: 14px;
        touch-action: none;
    }

    .ws-table {
        border-collapse: collapse;
        margin: auto;
    }

    .ws-cell {
        width: 30px;
        height: 30px;
        border: 1px solid #1e293b;
        text-align: center;
        vertical-align: middle;
        font-family: 'JetBrains Mono', monospace;
        font-size: 14px;
        font-weight: 700;
        color: #cbd5e1;
        cursor: pointer;
        transition: background 0.15s ease, transform 0.1s ease;
    }

    .ws-cell.selecting {
        background-color: #38bdf8 !important;
        color: #0b1120 !important;
        border-radius: 4px;
        transform: scale(1.08);
    }

    .ws-cell.found-vert {
        background-color: #059669;
        color: #ffffff;
        border-radius: 3px;
    }

    .ws-cell.found-horiz {
        background-color: #0284c7;
        color: #ffffff;
        border-radius: 3px;
    }

    .ws-cell.found-cross {
        background-color: #8b5cf6;
        color: #ffffff;
        border-radius: 3px;
    }

    /* Kelime Bankası */
    .word-bank-header {
        font-size: 12px;
        font-weight: 700;
        color: #94a3b8;
        letter-spacing: 0.5px;
        text-transform: uppercase;
        margin: 6px 0 8px 0;
    }

    .word-chips-container {
        display: flex;
        flex-wrap: wrap;
        gap: 6px;
        margin-bottom: 10px;
    }

    .word-chip {
        background-color: #1e293b;
        border: 1px solid #334155;
        border-radius: 6px;
        padding: 5px 9px;
        font-size: 11.5px;
        font-weight: 600;
        color: #94a3b8;
        display: flex;
        align-items: center;
        gap: 6px;
        transition: all 0.2s;
    }

    .word-chip.found {
        background-color: rgba(56, 189, 248, 0.18);
        border-color: #38bdf8;
        color: #f8fafc;
        box-shadow: 0 0 10px rgba(56, 189, 248, 0.3);
    }

    .word-chip.placed {
        background-color: rgba(34, 197, 94, 0.2);
        border-color: #22c55e;
        color: #86efac;
        text-decoration: line-through;
    }

    /* Sürüklenebilir Palet */
    .tokens-tray-title {
        font-size: 12px;
        font-weight: 700;
        color: #38bdf8;
        margin: 8px 0 6px 0;
        display: flex;
        align-items: center;
        gap: 6px;
    }

    .tokens-tray {
        min-height: 48px;
        background-color: #0b1120;
        border: 1px dashed #334155;
        border-radius: 8px;
        padding: 6px;
        display: flex;
        flex-wrap: wrap;
        gap: 6px;
        align-items: center;
    }

    .drag-token {
        background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%);
        color: #ffffff;
        border: 1px solid #38bdf8;
        border-radius: 6px;
        padding: 5px 10px;
        font-size: 11px;
        font-weight: 700;
        cursor: grab;
        display: inline-flex;
        align-items: center;
        gap: 5px;
        box-shadow: 0 3px 6px rgba(0, 0, 0, 0.3);
        touch-action: none;
    }

    .drag-token:active {
        cursor: grabbing;
        opacity: 0.7;
    }

    .drag-token.inhibitor {
        background: linear-gradient(135deg, #dc2626 0%, #991b1b 100%);
        border-color: #f87171;
    }

    .drag-token.cofactor {
        background: linear-gradient(135deg, #7c3aed 0%, #5b21b6 100%);
        border-color: #c084fc;
    }

    /* =========================================================
       SAĞ TARAF: PDH KÖPRÜSÜ & KREBS SİKLUSU ŞEMASI
       ========================================================= */
    .diagram-container {
        display: flex;
        flex-direction: column;
        gap: 12px;
        position: relative;
    }

    /* PDH Üst Blok */
    .pdh-bridge-box {
        background: linear-gradient(180deg, #1e293b 0%, #0f172a 100%);
        border: 2px solid #38bdf8;
        border-radius: 12px;
        padding: 12px 16px;
        position: relative;
    }

    .pdh-bridge-box::after {
        content: '▼';
        position: absolute;
        bottom: -14px;
        left: 50%;
        transform: translateX(-50%);
        color: #38bdf8;
        font-size: 12px;
    }

    .pdh-title-bar {
        font-size: 12px;
        font-weight: 700;
        color: #38bdf8;
        letter-spacing: 0.8px;
        text-transform: uppercase;
        margin-bottom: 8px;
        display: flex;
        justify-content: space-between;
    }

    .pdh-flow {
        display: flex;
        align-items: center;
        justify-content: space-around;
        gap: 8px;
    }

    .fixed-node {
        background-color: #0b1120;
        border: 1px solid #334155;
        border-radius: 8px;
        padding: 6px 12px;
        font-size: 12px;
        font-weight: 700;
        color: #94a3b8;
        text-align: center;
    }

    .fixed-node strong {
        color: #f8fafc;
        display: block;
        font-size: 13px;
    }

    /* Döngü Çerçevesi */
    .krebs-cycle-stage {
        position: relative;
        width: 100%;
        height: 620px;
        background: radial-gradient(circle at center, rgba(56, 189, 248, 0.05) 0%, rgba(15, 23, 42, 0.95) 75%);
        border: 1px solid #1e293b;
        border-radius: 16px;
        overflow: hidden;
    }

    /* Döngü Merkezi */
    .cycle-center-badge {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 150px;
        height: 150px;
        background-color: #0b1120;
        border: 2px solid #38bdf8;
        border-radius: 50%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        box-shadow: 0 0 25px rgba(56, 189, 248, 0.15);
        z-index: 1;
        padding: 10px;
    }

    .cycle-center-badge h3 {
        margin: 0;
        font-size: 14px;
        color: #f8fafc;
        font-family: 'Space Grotesk', sans-serif;
    }

    .cycle-center-badge span {
        font-size: 11px;
        color: #38bdf8;
        margin-top: 4px;
        font-weight: 600;
    }

    /* Dairesel SVG Ok Yolu */
    .cycle-svg {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 0;
    }

    /* Bırakma Alanları (Drop Zones) */
    .drop-zone {
        position: absolute;
        background-color: #1e293b;
        border: 2px dashed #475569;
        border-radius: 8px;
        padding: 6px 10px;
        min-width: 120px;
        min-height: 42px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        z-index: 2;
        transition: all 0.2s ease;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.4);
    }

    .drop-zone.hovered {
        border-color: #38bdf8;
        background-color: rgba(56, 189, 248, 0.15);
        transform: scale(1.05);
    }

    .drop-zone.correct {
        border-style: solid;
        border-color: #22c55e;
        background-color: rgba(34, 197, 94, 0.15);
        box-shadow: 0 0 12px rgba(34, 197, 94, 0.35);
    }

    .drop-zone.inhibitor-zone {
        border-color: #ef4444;
        background-color: rgba(239, 68, 68, 0.08);
    }

    .drop-zone.inhibitor-zone.correct {
        border-style: solid;
        border-color: #ef4444;
        background-color: rgba(239, 68, 68, 0.25);
        box-shadow: 0 0 12px rgba(239, 68, 68, 0.4);
    }

    .drop-label {
        font-size: 10px;
        color: #94a3b8;
        font-weight: 600;
        letter-spacing: 0.4px;
        pointer-events: none;
    }

    .placed-item {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 12px;
        font-weight: 700;
        color: #f8fafc;
        margin-top: 2px;
    }

    /* Konumlandırmalar (8 Saat Pozisyonu) */
    /* Saat 12 (Üst Merkez): Asetil-KoA / Sitrat Sentaz Girişi */
    #slot-asetilkoa { top: 12px; left: 50%; transform: translateX(-50%); }
    
    /* Saat 1: Sitrat */
    #slot-sitrat { top: 40px; right: 18%; }
    
    /* İnhibitör: Floroasetat (Akonitaz Yanı) */
    #slot-floroasetat { top: 120px; right: 2%; min-width: 100px; }
    
    /* Saat 2.5: İzositrat */
    #slot-izositrat { top: 180px; right: 10%; }
    
    /* Saat 4.5: Alfa-Ketoglutarat */
    #slot-alfaketoglutarat { bottom: 220px; right: 8%; }
    
    /* Saat 5.5: Süksinil-KoA */
    #slot-suksinilkoa { bottom: 80px; right: 22%; }
    
    /* Saat 6 (Alt Merkez): Süksinat */
    #slot-suksinat { bottom: 20px; left: 50%; transform: translateX(-50%); }
    
    /* İnhibitör: Malonat (SDH Yanı) */
    #slot-malonat { bottom: 95px; left: 6%; min-width: 95px; }

    /* Saat 7.5: Fumarat */
    #slot-fumarat { bottom: 150px; left: 14%; }
    
    /* Saat 9.5: Malat */
    #slot-malat { top: 250px; left: 8%; }
    
    /* Saat 11: Oksaloasetat */
    #slot-oksaloasetat { top: 80px; left: 18%; }

    /* Geri Bildirim Bannerı */
    .toast-message {
        margin-top: 10px;
        padding: 8px 14px;
        border-radius: 8px;
        font-size: 13px;
        text-align: center;
        background-color: #1e293b;
        border: 1px solid #334155;
        color: #38bdf8;
        min-height: 38px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 500;
    }

    /* Modal / Tebrik Kutusu */
    .completion-overlay {
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background: rgba(11, 17, 32, 0.9);
        display: none;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        z-index: 100;
        border-radius: 16px;
    }
    .completion-overlay.show { display: flex; }
    .completion-box {
        background: #0f172a;
        border: 2px solid #22c55e;
        border-radius: 16px;
        padding: 30px;
        text-align: center;
        max-width: 480px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.7);
    }
    .completion-box h2 {
        color: #4ade80;
        font-size: 28px;
        margin: 0 0 10px 0;
        font-family: 'Space Grotesk', sans-serif;
    }
    .restart-btn {
        background: #38bdf8;
        color: #0b1120;
        border: none;
        padding: 10px 24px;
        font-weight: 700;
        border-radius: 30px;
        cursor: pointer;
        margin-top: 16px;
        font-size: 14px;
    }
</style>
</head>
<body>

<div class="app-wrapper">

    <!-- SOL SÜTUN: KELİME AVI -->
    <div class="panel-card">
        <div class="panel-header">
            <h2 class="panel-title"><i class="fa-solid fa-magnifying-glass"></i> Kelime Avı Matrisi</h2>
            <div class="score-badge" id="word-score">0 / 14 Bulundu</div>
        </div>

        <div class="grid-container" id="grid-wrapper">
            <table class="ws-table" id="wordsearch-table"></table>
        </div>

        <div class="word-bank-header"><i class="fa-solid fa-arrows-up-down"></i> Dikey & <i class="fa-solid fa-arrows-left-right"></i> Yatay Hedef Kelimeler</div>
        <div class="word-chips-container" id="word-bank-chips"></div>

        <div class="tokens-tray-title">
            <i class="fa-solid fa-hand-pointer"></i> Şemaya Yerleştirilecek Parçalar
            <span style="font-size:10.5px; color:#94a3b8; font-weight:normal; margin-left:auto;">(Sürükleyin veya Tıklayın)</span>
        </div>
        <div class="tokens-tray" id="tokens-tray">
            <span style="color:#64748b; font-size:11.5px; padding:6px;">Bulduğunuz terimler burada açılacaktır...</span>
        </div>

        <div class="toast-message" id="toast-text">
            Harfleri fareyle ya da parmağınızla kaydırarak ilk kelimenizi bulun.
        </div>
    </div>

    <!-- SAĞ SÜTUN: PDH VE KREBS ŞEMASI -->
    <div class="panel-card">
        <div class="panel-header">
            <h2 class="panel-title"><i class="fa-solid fa-circle-nodes"></i> PDH & Krebs Döngüsü Sürükle-Bırak Şeması</h2>
            <div class="score-badge" id="drop-score" style="color:#22c55e; border-color:rgba(34,197,94,0.3); background:rgba(34,197,94,0.12);">
                0 / 11 Yerleşti
            </div>
        </div>

        <div class="diagram-container">
            
            <!-- PDH Giriş Köprüsü -->
            <div class="pdh-bridge-box">
                <div class="pdh-title-bar">
                    <span>PİRUVAT DEHİDROJENAZ (PDH) KÖPRÜSÜ</span>
                    <span style="color:#f87171;"><i class="fa-solid fa-triangle-exclamation"></i> Kofaktör & İnhibitör İstasyonu</span>
                </div>
                <div class="pdh-flow">
                    <div class="fixed-node">Glikolizden<br><strong>PİRUVAT (3C)</strong></div>
                    <i class="fa-solid fa-arrow-right" style="color:#38bdf8;"></i>
                    <div class="drop-zone inhibitor-zone" id="slot-arsenik" data-accept="ARSENİK" style="position:static; min-width:110px;">
                        <span class="drop-label">[İNHİBİTÖR]</span>
                        <span class="placed-item">?</span>
                    </div>
                    <div class="drop-zone" id="slot-tiamin" data-accept="TİAMİN" style="position:static; min-width:110px;">
                        <span class="drop-label">[E1 KOFAKTÖRÜ]</span>
                        <span class="placed-item">?</span>
                    </div>
                    <div class="drop-zone" id="slot-lipoikasit" data-accept="LİPOİKASİT" style="position:static; min-width:110px;">
                        <span class="drop-label">[E2 KOFAKTÖRÜ]</span>
                        <span class="placed-item">?</span>
                    </div>
                    <i class="fa-solid fa-arrow-right" style="color:#38bdf8;"></i>
                    <div class="drop-zone" id="slot-asetilkoa" data-accept="KOENZİMA" style="position:static; min-width:110px;">
                        <span class="drop-label">[DÖNGÜYE GİRİŞ]</span>
                        <span class="placed-item">ASETİL-KoA</span>
                    </div>
                </div>
            </div>

            <!-- Dairesel Krebs Döngüsü Sahnesi -->
            <div class="krebs-cycle-stage" id="cycle-stage">

                <svg class="cycle-svg" viewBox="0 0 700 620">
                    <defs>
                        <linearGradient id="orbit-gradient" x1="0%" y1="0%" x2="100%" y2="100%">
                            <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.8"/>
                            <stop offset="50%" stop-color="#818cf8" stop-opacity="0.4"/>
                            <stop offset="100%" stop-color="#38bdf8" stop-opacity="0.8"/>
                        </linearGradient>
                        <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                            <path d="M 0 0 L 10 5 L 0 10 z" fill="#38bdf8"/>
                        </marker>
                    </defs>
                    <!-- Ana Döngü Çemberi -->
                    <circle cx="350" cy="310" r="220" fill="none" stroke="url(#orbit-gradient)" stroke-width="3" stroke-dasharray="8 6" />
                    <!-- Akış Okları -->
                    <path d="M 350 90 A 220 220 0 0 1 570 310" fill="none" stroke="#38bdf8" stroke-width="3" marker-end="url(#arrow)"/>
                    <path d="M 570 310 A 220 220 0 0 1 350 530" fill="none" stroke="#38bdf8" stroke-width="3" marker-end="url(#arrow)"/>
                    <path d="M 350 530 A 220 220 0 0 1 130 310" fill="none" stroke="#38bdf8" stroke-width="3" marker-end="url(#arrow)"/>
                    <path d="M 130 310 A 220 220 0 0 1 350 90" fill="none" stroke="#38bdf8" stroke-width="3" marker-end="url(#arrow)"/>
                </svg>

                <!-- Merkez Rozeti -->
                <div class="cycle-center-badge">
                    <i class="fa-solid fa-atom" style="font-size:24px; color:#38bdf8; margin-bottom:4px;"></i>
                    <h3>SİTRİK ASİT SİKLUSU</h3>
                    <span>1 Tur = 10 ATP</span>
                    <span style="color:#94a3b8; font-size:9.5px;">(3 NADH, 1 FADH2, 1 GTP)</span>
                </div>

                <!-- 8 Reaksiyon Basamağı Drop Zoneları -->
                <!-- 1. SİTRAT -->
                <div class="drop-zone" id="slot-sitrat" data-accept="SİTRAT" style="top:45px; right:150px;">
                    <span class="drop-label">1. BASAMAK (6C)</span>
                    <span class="placed-item">?</span>
                </div>

                <!-- İNHİBİTÖR: FLOROASETAT (Akonitaz Bloker) -->
                <div class="drop-zone inhibitor-zone" id="slot-floroasetat" data-accept="FLOROASETAT" style="top:115px; right:15px;">
                    <span class="drop-label">[ÖLÜMCÜL SENTEZ]</span>
                    <span class="placed-item">İnhibitör ?</span>
                </div>

                <!-- 2. İZOSİTRAT -->
                <div class="drop-zone" id="slot-izositrat" data-accept="İZOSİTRAT" style="top:210px; right:45px;">
                    <span class="drop-label">2. BASAMAK (6C)</span>
                    <span class="placed-item">?</span>
                </div>

                <!-- 3. ALFA-KETOGLUTARAT -->
                <div class="drop-zone" id="slot-alfaketoglutarat" data-accept="ALFAKETOGLUTARAT" style="bottom:190px; right:40px;">
                    <span class="drop-label">3. BASAMAK (5C)</span>
                    <span class="placed-item">α-Ketoglutarat</span>
                </div>

                <!-- 4. SÜKSİNİL-KoA -->
                <div class="drop-zone" id="slot-suksinilkoa" data-accept="SÜKSİNİLKOA" style="bottom:75px; right:140px;">
                    <span class="drop-label">4. BASAMAK (4C)</span>
                    <span class="placed-item">?</span>
                </div>

                <!-- 5. SÜKSİNAT -->
                <div class="drop-zone" id="slot-suksinat" data-accept="SÜKSİNAT" style="bottom:18px; left:50%; transform:translateX(-50%);">
                    <span class="drop-label">5. BASAMAK (GTP)</span>
                    <span class="placed-item">?</span>
                </div>

                <!-- İNHİBİTÖR: MALONAT (Kompleks II Bloker) -->
                <div class="drop-zone inhibitor-zone" id="slot-malonat" data-accept="MALONAT" style="bottom:90px; left:25px;">
                    <span class="drop-label">[KOMPETİTİF İNH.]</span>
                    <span class="placed-item">İnhibitör ?</span>
                </div>

                <!-- 6. FUMARAT -->
                <div class="drop-zone" id="slot-fumarat" data-accept="FUMARAT" style="bottom:180px; left:80px;">
                    <span class="drop-label">6. BASAMAK (FADH2)</span>
                    <span class="placed-item">?</span>
                </div>

                <!-- 7. MALAT -->
                <div class="drop-zone" id="slot-malat" data-accept="MALAT" style="top:230px; left:50px;">
                    <span class="drop-label">7. BASAMAK (4C)</span>
                    <span class="placed-item">?</span>
                </div>

                <!-- 8. OKSALOASETAT -->
                <div class="drop-zone" id="slot-oksaloasetat" data-accept="OKSALOASETAT" style="top:55px; left:140px;">
                    <span class="drop-label">8. BASAMAK (REJENERASYON)</span>
                    <span class="placed-item">?</span>
                </div>

            </div>

        </div>

    </div>

</div>

<!-- Kutlama Modalı -->
<div class="completion-overlay" id="modal-success">
    <div class="completion-box">
        <i class="fa-solid fa-trophy" style="font-size: 54px; color:#fbbf24; margin-bottom:14px;"></i>
        <h2>Tebrikler Hekim Adayı!</h2>
        <p style="color:#cbd5e1; font-size:14px; line-height:1.6;">
            Krebs döngüsü ve PDH kavşağındaki tüm metabolitleri, kofaktörleri ve toksikolojik blokaj noktalarını başarıyla tespit edip yerleştirdiniz!
        </p>
        <button class="restart-btn" onclick="location.reload();">Tekrar Çöz</button>
    </div>
</div>

<script>
/* =========================================================================
   1. HARF MATRİSİ VE GİZLİ KELİME VERİLERİ (YATAY & DİKEY DÜZEN)
   ========================================================================= */
const GRID_DATA = [
    ['O','S','İ','T','R','A','T','B','F','A','D','Z','P','K'],
    ['K','T','İ','A','M','İ','N','C','L','N','A','D','H','R'],
    ['S','E','Z','V','Y','B','S','D','O','M','F','G','C','T'],
    ['A','K','O','P','S','L','Ü','R','R','H','U','B','E','N'],
    ['L','O','S','G','Ü','T','K','B','O','N','M','E','S','D'],
    ['O','E','İ','M','K','D','S','K','A','P','A','R','V','Z'],
    ['A','N','T','Y','S','R','İ','L','S','C','R','İ','M','Y'],
    ['S','Z','R','F','İ','H','N','P','E','D','A','B','A','G'],
    ['E','İ','A','B','N','G','İ','T','T','L','T','E','L','C'],
    ['T','M','T','H','A','V','L','S','A','E','B','R','A','F'],
    ['A','A','P','K','T','D','K','R','T','M','C','İ','T','H'],
    ['T','B','L','G','C','N','O','M','A','L','O','N','A','T'],
    ['L','İ','P','O','İ','K','A','S','İ','T','F','Z','K','Y'],
    ['D','A','R','S','E','N','İ','K','G','V','T','P','P','M']
];

// Aranan Kelimeler Kataloğu
const WORDS_TO_FIND = [
    // DİKEYLER
    { word: "OKSALOASETAT", dir: "vert", r1:0, c1:0, r2:11, c2:0, found: false, placed: false, role: "cycle" },
    { word: "KOENZİMA",     dir: "vert", r1:3, c1:1, r2:10, c2:1, found: false, placed: false, role: "pdh" },
    { word: "İZOSİTRAT",    dir: "vert", r1:1, c1:2, r2:9,  c2:2, found: false, placed: false, role: "cycle" },
    { word: "SÜKSİNAT",     dir: "vert", r1:3, c1:4, r2:10, c2:4, found: false, placed: false, role: "cycle" },
    { word: "SÜKSİNİLKOA",  dir: "vert", r1:2, c1:6, r2:12, c2:6, found: false, placed: false, role: "cycle" },
    { word: "FLOROASETAT",  dir: "vert", r1:0, c1:8, r2:10, c2:8, found: false, placed: false, role: "inhibitor" },
    { word: "FUMARAT",      dir: "vert", r1:2, c1:10,r2:8,  c2:10,found: false, placed: false, role: "cycle" },
    { word: "BERİBERİ",     dir: "vert", r1:3, c1:11,r2:10, c2:11,found: false, placed: false, role: "clinical" },
    { word: "MALAT",        dir: "vert", r1:6, c1:12,r2:10, c2:12,found: false, placed: false, role: "cycle" },
    // YATAYLAR
    { word: "SİTRAT",       dir: "horiz",r1:0, c1:1, r2:0,  c2:6, found: false, placed: false, role: "cycle" },
    { word: "FAD",          dir: "horiz",r1:0, c1:8, r2:0,  c2:10,found: false, placed: false, role: "cofactor" },
    { word: "TİAMİN",       dir: "horiz",r1:1, c1:1, r2:1,  c2:6, found: false, placed: false, role: "cofactor" },
    { word: "NADH",         dir: "horiz",r1:1, c1:9, r2:1,  c2:12,found: false, placed: false, role: "cofactor" },
    { word: "MALONAT",      dir: "horiz",r1:11,c1:7, r2:11, c2:13,found: false, placed: false, role: "inhibitor" },
    { word: "LİPOİKASİT",   dir: "horiz",r1:12,c1:0, r2:12, c2:9, found: false, placed: false, role: "cofactor" },
    { word: "ARSENİK",      dir: "horiz",r1:13,c1:1, r2:13, c2:7, found: false, placed: false, role: "inhibitor" },
    { word: "TPP",          dir: "horiz",r1:13,c1:10,r2:13, c2:12,found: false, placed: false, role: "cofactor" }
];

let isSelecting = false;
let startCell = null;
let selectedCells = [];
let foundWordsCount = 0;
let placedTokensCount = 0;
let selectedTokenForPlacement = null; // Mobil için tıklayarak yerleştirme

/* =========================================================================
   2. MATRİS VE KELİME LİSTESİ OLUŞTURMA
   ========================================================================= */
const table = document.getElementById("wordsearch-table");
const chipsContainer = document.getElementById("word-bank-chips");
const tokensTray = document.getElementById("tokens-tray");

// Tabloyu DOM'a dökme
GRID_DATA.forEach((row, r) => {
    const tr = document.createElement("tr");
    row.forEach((char, c) => {
        const td = document.createElement("td");
        td.className = "ws-cell";
        td.innerText = char;
        td.dataset.row = r;
        td.dataset.col = c;
        tr.appendChild(td);
    });
    table.appendChild(tr);
});

// Kelime Etiketlerini Çizme
WORDS_TO_FIND.forEach(w => {
    const chip = document.createElement("span");
    chip.className = "word-chip";
    chip.id = `chip-${w.word}`;
    chip.innerHTML = `${w.dir === 'vert' ? '<i class="fa-solid fa-arrow-down"></i>' : '<i class="fa-solid fa-arrow-right"></i>'} ${w.word}`;
    chipsContainer.appendChild(chip);
});

/* =========================================================================
   3. SEÇİM MANTIĞI: HEM FARE (MOUSE) HEM DOKUNMATİK (TOUCH / TABLET)
   ========================================================================= */
function getCellFromPoint(x, y) {
    const el = document.elementFromPoint(x, y);
    if (el && el.classList.contains("ws-cell")) {
        return el;
    }
    return null;
}

function handleSelectionStart(cell) {
    if (!cell) return;
    isSelecting = true;
    startCell = cell;
    selectedCells = [cell];
    clearSelectionStyles();
    cell.classList.add("selecting");
}

function handleSelectionMove(cell) {
    if (!isSelecting || !startCell || !cell) return;
    
    const r1 = parseInt(startCell.dataset.row);
    const c1 = parseInt(startCell.dataset.col);
    const r2 = parseInt(cell.dataset.row);
    const c2 = parseInt(cell.dataset.col);

    // Yalnızca düz yatay veya düz dikey seçime izin ver
    const isHoriz = (r1 === r2);
    const isVert = (c1 === c2);

    if (!isHoriz && !isVert) return;

    clearSelectionStyles();
    selectedCells = [];

    const minR = Math.min(r1, r2);
    const maxR = Math.max(r1, r2);
    const minC = Math.min(c1, c2);
    const maxC = Math.max(c1, c2);

    for (let r = minR; r <= maxR; r++) {
        for (let c = minC; c <= maxC; c++) {
            const current = table.rows[r].cells[c];
            current.classList.add("selecting");
            selectedCells.push(current);
        }
    }
}

function handleSelectionEnd() {
    if (!isSelecting) return;
    isSelecting = false;

    if (selectedCells.length >= 3) {
        // Seçilen harfleri topla
        const letters = selectedCells.map(td => td.innerText).join("");
        const revLetters = letters.split("").reverse().join("");

        // Eşleşme kontrolü
        let match = WORDS_TO_FIND.find(w => !w.found && (w.word === letters || w.word === revLetters));

        if (match) {
            match.found = true;
            foundWordsCount++;
            document.getElementById("word-score").innerText = `${foundWordsCount} / ${WORDS_TO_FIND.length} Bulundu`;

            // Hücreleri kalıcı boya
            selectedCells.forEach(td => {
                if (td.classList.contains("found-vert") || td.classList.contains("found-horiz")) {
                    td.classList.remove("found-vert", "found-horiz");
                    td.classList.add("found-cross");
                } else {
                    td.classList.add(match.dir === "vert" ? "found-vert" : "found-horiz");
                }
            });

            // Chip'i aktifleştir
            const chip = document.getElementById(`chip-${match.word}`);
            if (chip) chip.classList.add("found");

            // Sürükle bırak tepsisine token ekle
            createDraggableToken(match);

            showToast(`Harika! "${match.word}" bulundu. Şimdi sağdaki şemaya yerleştirin.`, "#38bdf8");
            playSuccessSound();
        }
    }
    clearSelectionStyles();
}

function clearSelectionStyles() {
    const allSelecting = table.querySelectorAll(".selecting");
    allSelecting.forEach(td => td.classList.remove("selecting"));
}

// Mouse Olayları
table.addEventListener("mousedown", (e) => {
    if (e.target.classList.contains("ws-cell")) {
        handleSelectionStart(e.target);
    }
});

window.addEventListener("mousemove", (e) => {
    if (isSelecting) {
        const cell = getCellFromPoint(e.clientX, e.clientY);
        handleSelectionMove(cell);
    }
});

window.addEventListener("mouseup", handleSelectionEnd);

// Touch / Dokunmatik Ekran Olayları (Tablet & Telefon)
table.addEventListener("touchstart", (e) => {
    const touch = e.touches[0];
    const cell = getCellFromPoint(touch.clientX, touch.clientY);
    if (cell) {
        e.preventDefault();
        handleSelectionStart(cell);
    }
}, { passive: false });

window.addEventListener("touchmove", (e) => {
    if (isSelecting) {
        const touch = e.touches[0];
        const cell = getCellFromPoint(touch.clientX, touch.clientY);
        if (cell) {
            handleSelectionMove(cell);
        }
    }
}, { passive: false });

window.addEventListener("touchend", handleSelectionEnd);

/* =========================================================================
   4. SÜRÜKLE - BIRAK VE DOKUNARAK YERLEŞTİRME SİSTEMİ
   ========================================================================= */
function createDraggableToken(match) {
    // Boş tepsi uyarısını kaldır
    if (tokensTray.querySelector("span")) {
        tokensTray.innerHTML = "";
    }

    const token = document.createElement("div");
    token.className = `drag-token ${match.role}`;
    token.id = `token-${match.word}`;
    token.draggable = true;
    token.innerHTML = `<i class="fa-solid fa-cube"></i> ${match.word}`;
    token.dataset.word = match.word;

    // HTML5 Drag Events (Masaüstü)
    token.addEventListener("dragstart", (e) => {
        e.dataTransfer.setData("text/plain", match.word);
        token.style.opacity = "0.5";
    });

    token.addEventListener("dragend", () => {
        token.style.opacity = "1";
    });

    // Mobil Tıkla-Seç Mekanizması
    token.addEventListener("click", () => {
        document.querySelectorAll(".drag-token").forEach(t => t.style.outline = "none");
        selectedTokenForPlacement = match.word;
        token.style.outline = "2px solid #facc15";
        showToast(`"${match.word}" seçildi. Şimdi yerleştirmek istediğiniz kutucuğa tıklayın.`, "#facc15");
    });

    tokensTray.appendChild(token);
}

// Bırakma Alanlarını (Drop Zones) Dinleme
const dropZones = document.querySelectorAll(".drop-zone");

dropZones.forEach(zone => {
    // Sürükleme Üzerine Geldiğinde
    zone.addEventListener("dragover", (e) => {
        e.preventDefault();
        zone.classList.add("hovered");
    });

    zone.addEventListener("dragleave", () => {
        zone.classList.remove("hovered");
    });

    // Masaüstü Bırakma
    zone.addEventListener("drop", (e) => {
        e.preventDefault();
        zone.classList.remove("hovered");
        const droppedWord = e.dataTransfer.getData("text/plain");
        checkAndPlaceToken(zone, droppedWord);
    });

    // Mobil Tıklama ile Yerleştirme
    zone.addEventListener("click", () => {
        if (selectedTokenForPlacement) {
            checkAndPlaceToken(zone, selectedTokenForPlacement);
            selectedTokenForPlacement = null;
            document.querySelectorAll(".drag-token").forEach(t => t.style.outline = "none");
        }
    });
});

function checkAndPlaceToken(zone, word) {
    const expected = zone.dataset.accept;

    if (expected === word) {
        // DOĞRU YERLEŞTİRME
        zone.classList.add("correct");
        zone.querySelector(".placed-item").innerText = word;

        // Token'ı tepsiden gizle
        const tokenElem = document.getElementById(`token-${word}`);
        if (tokenElem) tokenElem.style.display = "none";

        // Chip'i tamamlandı yap
        const chip = document.getElementById(`chip-${word}`);
        if (chip) chip.classList.add("placed");

        placedTokensCount++;
        document.getElementById("drop-score").innerText = `${placedTokensCount} / 11 Yerleşti`;

        showToast(`Harika! ${word} doğru basamağa yerleştirildi.`, "#22c55e");
        playSnapSound();

        // Hepsi bitti mi?
        if (placedTokensCount >= 11) {
            setTimeout(() => {
                document.getElementById("modal-success").classList.add("show");
            }, 600);
        }
    } else {
        // YANLIŞ YERLEŞTİRME
        zone.style.animation = "shake 0.3s ease";
        setTimeout(() => zone.style.animation = "", 350);
        showToast(`Bu basamak "${word}" için uygun değil. İpuçlarını kontrol edin!`, "#ef4444");
    }
}

function showToast(msg, color="#38bdf8") {
    const toast = document.getElementById("toast-text");
    toast.style.borderColor = color;
    toast.style.color = color;
    toast.innerText = msg;
}

/* =========================================================================
   5. WEB AUDIO API İLE SES GERİ BİLDİRİMİ (MİNİMAL VE ZARİF)
   ========================================================================= */
let audioCtx = null;
function initAudio() {
    if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
}

function playSuccessSound() {
    try {
        initAudio();
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = "sine";
        osc.frequency.setValueAtTime(523.25, audioCtx.currentTime); // C5
        osc.frequency.exponentialRampToValueAtTime(783.99, audioCtx.currentTime + 0.2); // G5
        gain.gain.setValueAtTime(0.15, audioCtx.currentTime);
        gain.gain.linearRampToValueAtTime(0.01, audioCtx.currentTime + 0.25);
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start();
        osc.stop(audioCtx.currentTime + 0.25);
    } catch(e){}
}

function playSnapSound() {
    try {
        initAudio();
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = "triangle";
        osc.frequency.setValueAtTime(440, audioCtx.currentTime);
        osc.frequency.linearRampToValueAtTime(880, audioCtx.currentTime + 0.15);
        gain.gain.setValueAtTime(0.2, audioCtx.currentTime);
        gain.gain.linearRampToValueAtTime(0.01, audioCtx.currentTime + 0.18);
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start();
        osc.stop(audioCtx.currentTime + 0.18);
    } catch(e){}
}
</script>

</body>
</html>
"""

# Streamlit Bileşeni Olarak Render Et
components.html(interactive_app_code, height=940, scrolling=False)
