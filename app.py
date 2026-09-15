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
    <p>Sol taraftaki <strong>Kelime Avı</strong>'nda yatay ve dikey gizlenmiş 17 metabolit, kofaktör ve klinik terimi bulun; açılan parçaları sağdaki <strong>PDH Köprüsü ve Dairesel Krebs Siklusu</strong> hedef alanlarına yerleştirin.</p>
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
    Soldaki matriste fareyle sürükleyerek veya dokunmatik ekranda parmağınızı kaydırarak aranan kelimeleri bulun.
    2. **Şemayı Tamamlayın (17 Hedef Alan):**  
    • **PDH İstasyonu:** Tiamin, TPP, Koenzim A, Lipoik Asit, FAD, NADH  
    • **Klinik Blokajlar:** Arsenik, Beriberi, Floroasetat, Malonat  
    • **Krebs Siklusu:** Sitrat, İzositrat, Süksinil-KoA, Süksinat, Fumarat, Malat, Oksaloasetat  
    3. **Mobil Uyumluluk:**  
    Masaüstünde parçayı sürükleyip bırakabilir; mobil cihazlarda açılan parçaya dokunup ardından gitmesi gereken kutucuğa tıklayarak da yerleştirebilirsiniz.
    """)
    st.divider()

    st.subheader("📚 TUS & Komite Kodlamaları")
    with st.expander("PDH 5 Kofaktörü"):
        st.write("**Tenha Lokantada Köfte, Fasulye, Nohut**")
        st.caption("TPP (B1), Lipoik Asit, KoA (B5), FAD (B2), NAD⁺ (B3)")
    with st.expander("Siklus Ara Ürünleri"):
        st.write("**Sonunda İki Kardeş Fırından Malatya Otlu Ekmeği Aldı**")
        st.caption("Sitrat → İzositrat → α-KG → Süksinil-KoA → Süksinat → Fumarat → Malat → Oksaloasetat")
    with st.expander("Klinik Blokajlar & Toksinler"):
        st.write("• **Arsenik:** E2 lipoik asidin -SH gruplarını bağlar.")
        st.write("• **Beriberi:** B1 (Tiamin/TPP) eksikliğinde E1 durur.")
        st.write("• **Floroasetat:** Florositrata döner; akonitazı bloke eder.")
        st.write("• **Malonat:** Kompleks II'yi (SDH) kompetitif inhibe eder.")

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
        grid-template-columns: 480px 1fr;
        gap: 18px;
        width: 100%;
        min-height: 980px;
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
        padding: 16px;
        box-shadow: 0 12px 30px rgba(0, 0, 0, 0.4);
        display: flex;
        flex-direction: column;
    }

    .panel-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 12px;
        border-bottom: 1px solid #1e293b;
        padding-bottom: 8px;
    }

    .panel-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 17px;
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
        padding: 6px;
        margin-bottom: 12px;
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
        font-size: 13.5px;
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
        font-size: 11.5px;
        font-weight: 700;
        color: #94a3b8;
        letter-spacing: 0.5px;
        text-transform: uppercase;
        margin: 4px 0 6px 0;
    }

    .word-chips-container {
        display: flex;
        flex-wrap: wrap;
        gap: 5px;
        margin-bottom: 8px;
    }

    .word-chip {
        background-color: #1e293b;
        border: 1px solid #334155;
        border-radius: 6px;
        padding: 4px 8px;
        font-size: 11px;
        font-weight: 600;
        color: #94a3b8;
        display: flex;
        align-items: center;
        gap: 5px;
        transition: all 0.2s;
    }

    .word-chip.found {
        background-color: rgba(56, 189, 248, 0.18);
        border-color: #38bdf8;
        color: #f8fafc;
        box-shadow: 0 0 8px rgba(56, 189, 248, 0.3);
    }

    .word-chip.placed {
        background-color: rgba(34, 197, 94, 0.2);
        border-color: #22c55e;
        color: #86efac;
        text-decoration: line-through;
    }

    /* Sürüklenebilir Palet */
    .tokens-tray-title {
        font-size: 11.5px;
        font-weight: 700;
        color: #38bdf8;
        margin: 6px 0 6px 0;
        display: flex;
        align-items: center;
        gap: 6px;
    }

    .tokens-tray {
        min-height: 52px;
        background-color: #0b1120;
        border: 1px dashed #334155;
        border-radius: 8px;
        padding: 6px;
        display: flex;
        flex-wrap: wrap;
        gap: 5px;
        align-items: center;
    }

    .drag-token {
        background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%);
        color: #ffffff;
        border: 1px solid #38bdf8;
        border-radius: 6px;
        padding: 4px 9px;
        font-size: 11px;
        font-weight: 700;
        cursor: grab;
        display: inline-flex;
        align-items: center;
        gap: 5px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
        touch-action: none;
    }

    .drag-token:active {
        cursor: grabbing;
        opacity: 0.7;
    }

    .drag-token.inhibitor, .drag-token.clinical {
        background: linear-gradient(135deg, #dc2626 0%, #991b1b 100%);
        border-color: #f87171;
    }

    .drag-token.cofactor {
        background: linear-gradient(135deg, #7c3aed 0%, #5b21b6 100%);
        border-color: #c084fc;
    }

    .drag-token.pdh {
        background: linear-gradient(135deg, #0d9488 0%, #115e59 100%);
        border-color: #2dd4bf;
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
        border-radius: 14px;
        padding: 12px 14px;
        position: relative;
    }

    .pdh-bridge-box::after {
        content: '▼ SİKLUSA GİRİŞ';
        position: absolute;
        bottom: -13px;
        left: 50%;
        transform: translateX(-50%);
        color: #38bdf8;
        font-size: 10px;
        font-weight: 700;
        background: #0f172a;
        padding: 1px 8px;
        border-radius: 10px;
        border: 1px solid #38bdf8;
        z-index: 10;
    }

    .pdh-title-bar {
        font-size: 11px;
        font-weight: 700;
        color: #38bdf8;
        letter-spacing: 0.8px;
        text-transform: uppercase;
        margin-bottom: 8px;
        display: flex;
        justify-content: space-between;
    }

    .pdh-section-sub {
        font-size: 10px;
        font-weight: 700;
        color: #94a3b8;
        letter-spacing: 0.5px;
        text-transform: uppercase;
        margin: 6px 0 4px 0;
        display: flex;
        align-items: center;
        gap: 6px;
    }

    .pdh-flow-row {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 6px;
        flex-wrap: wrap;
    }

    .fixed-node {
        background-color: #0b1120;
        border: 1px solid #334155;
        border-radius: 8px;
        padding: 5px 9px;
        font-size: 11px;
        font-weight: 700;
        color: #94a3b8;
        text-align: center;
        flex-shrink: 0;
    }

    .fixed-node strong {
        color: #f8fafc;
        display: block;
        font-size: 12px;
    }

    /* Döngü Çerçevesi */
    .krebs-cycle-stage {
        position: relative;
        width: 100%;
        height: 610px;
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
        width: 140px;
        height: 140px;
        background-color: #0b1120;
        border: 2px solid #38bdf8;
        border-radius: 50%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        box-shadow: 0 0 22px rgba(56, 189, 248, 0.15);
        z-index: 1;
        padding: 8px;
    }

    .cycle-center-badge h3 {
        margin: 0;
        font-size: 13px;
        color: #f8fafc;
        font-family: 'Space Grotesk', sans-serif;
    }

    .cycle-center-badge span {
        font-size: 10.5px;
        color: #38bdf8;
        margin-top: 3px;
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
        padding: 4px 8px;
        min-width: 105px;
        min-height: 42px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        z-index: 2;
        transition: all 0.2s ease;
        box-shadow: 0 3px 8px rgba(0, 0, 0, 0.35);
        cursor: pointer;
    }

    .drop-zone.static-flow {
        position: static;
        flex: 1;
        min-width: 100px;
    }

    .drop-zone.hovered {
        border-color: #38bdf8;
        background-color: rgba(56, 189, 248, 0.2);
        transform: scale(1.04);
    }

    .drop-zone.correct {
        border-style: solid;
        border-color: #22c55e;
        background-color: rgba(34, 197, 94, 0.18);
        box-shadow: 0 0 10px rgba(34, 197, 94, 0.35);
    }

    .drop-zone.inhibitor-zone {
        border-color: #ef4444;
        background-color: rgba(239, 68, 68, 0.08);
    }

    .drop-zone.inhibitor-zone.correct {
        border-style: solid;
        border-color: #ef4444;
        background-color: rgba(239, 68, 68, 0.25);
        box-shadow: 0 0 10px rgba(239, 68, 68, 0.4);
    }

    .drop-label {
        font-size: 9px;
        color: #94a3b8;
        font-weight: 700;
        letter-spacing: 0.4px;
        pointer-events: none;
    }

    .placed-item {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 11.5px;
        font-weight: 700;
        color: #f8fafc;
        margin-top: 1px;
    }

    /* Geri Bildirim Bannerı */
    .toast-message {
        margin-top: 8px;
        padding: 7px 12px;
        border-radius: 8px;
        font-size: 12.5px;
        text-align: center;
        background-color: #1e293b;
        border: 1px solid #334155;
        color: #38bdf8;
        min-height: 36px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 500;
    }

    /* Modal / Tebrik Kutusu */
    .completion-overlay {
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background: rgba(11, 17, 32, 0.92);
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
        padding: 28px;
        text-align: center;
        max-width: 480px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.7);
    }
    .completion-box h2 {
        color: #4ade80;
        font-size: 26px;
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
        font-size: 13.5px;
    }
</style>
</head>
<body>

<div class="app-wrapper">

    <!-- SOL SÜTUN: KELİME AVI -->
    <div class="panel-card">
        <div class="panel-header">
            <h2 class="panel-title"><i class="fa-solid fa-magnifying-glass"></i> Kelime Avı Matrisi</h2>
            <div class="score-badge" id="word-score">0 / 17 Bulundu</div>
        </div>

        <div class="grid-container" id="grid-wrapper">
            <table class="ws-table" id="wordsearch-table"></table>
        </div>

        <div class="word-bank-header"><i class="fa-solid fa-arrows-up-down"></i> Dikey & <i class="fa-solid fa-arrows-left-right"></i> Yatay Hedef Terimler</div>
        <div class="word-chips-container" id="word-bank-chips"></div>

        <div class="tokens-tray-title">
            <i class="fa-solid fa-hand-pointer"></i> Şemaya Yerleştirilecek Parçalar
            <span style="font-size:10px; color:#94a3b8; font-weight:normal; margin-left:auto;">(Sürükleyin veya Tıklayın)</span>
        </div>
        <div class="tokens-tray" id="tokens-tray">
            <span style="color:#64748b; font-size:11px; padding:6px;">Bulduğunuz terimler burada açılacaktır...</span>
        </div>

        <div class="toast-message" id="toast-text">
            Harfleri fareyle ya da parmağınızla kaydırarak ilk teriminizi bulun.
        </div>
    </div>

    <!-- SAĞ SÜTUN: PDH VE KREBS ŞEMASI -->
    <div class="panel-card">
        <div class="panel-header">
            <h2 class="panel-title"><i class="fa-solid fa-circle-nodes"></i> PDH Köprüsü & Krebs Siklusu Şeması</h2>
            <div class="score-badge" id="drop-score" style="color:#22c55e; border-color:rgba(34,197,94,0.3); background:rgba(34,197,94,0.12);">
                0 / 17 Yerleşti
            </div>
        </div>

        <div class="diagram-container">
            
            <!-- PDH Giriş Köprüsü (Tüm Kofaktör, Koenzim ve Blokaj Noktaları) -->
            <div class="pdh-bridge-box">
                <div class="pdh-title-bar">
                    <span>PİRUVAT DEHİDROJENAZ (PDH) KÖPRÜSÜ</span>
                    <span style="color:#f87171;"><i class="fa-solid fa-triangle-exclamation"></i> 5 Kofaktör & Klinik Blokaj İstasyonu</span>
                </div>

                <!-- 1. Hat: Substrat, Koenzim A, NADH ve Ürün Akışı -->
                <div class="pdh-section-sub"><i class="fa-solid fa-arrow-right-arrow-left"></i> 1. Ana Akış & Koenzimler</div>
                <div class="pdh-flow-row">
                    <div class="fixed-node">Glikolizden<br><strong>PİRUVAT (3C)</strong></div>
                    <i class="fa-solid fa-plus" style="color:#38bdf8; font-size:11px;"></i>
                    <div class="drop-zone static-flow" id="slot-koenzima" data-accept="KOENZİMA">
                        <span class="drop-label">[AÇİL TAŞIYICI (B5)]</span>
                        <span class="placed-item">?</span>
                    </div>
                    <i class="fa-solid fa-arrow-right" style="color:#38bdf8; font-size:11px;"></i>
                    <div class="drop-zone static-flow" id="slot-nadh" data-accept="NADH">
                        <span class="drop-label">[İNDİRGENMİŞ ÜRÜN (B3)]</span>
                        <span class="placed-item">?</span>
                    </div>
                    <i class="fa-solid fa-arrow-right" style="color:#38bdf8; font-size:11px;"></i>
                    <div class="fixed-node" style="border-color:#38bdf8; background:rgba(56,189,248,0.1);">Siklusa Giriş<br><strong style="color:#38bdf8;">ASETİL-KoA (2C)</strong></div>
                </div>

                <!-- 2. Hat: E1, E2, E3 Kofaktörleri ve Toksikoloji / Patoloji -->
                <div class="pdh-section-sub" style="margin-top:8px;"><i class="fa-solid fa-dna"></i> 2. Enzim Kompleksleri (E1-E2-E3) & Klinik</div>
                <div class="pdh-flow-row">
                    <!-- E1 Kofaktörleri ve Klinik -->
                    <div class="drop-zone static-flow" id="slot-tiamin" data-accept="TİAMİN">
                        <span class="drop-label">[B1 VİTAMİNİ]</span>
                        <span class="placed-item">?</span>
                    </div>
                    <div class="drop-zone static-flow" id="slot-tpp" data-accept="TPP">
                        <span class="drop-label">[E1 AKTİF KOFAKTÖR]</span>
                        <span class="placed-item">?</span>
                    </div>
                    <div class="drop-zone static-flow inhibitor-zone" id="slot-beriberi" data-accept="BERİBERİ">
                        <span class="drop-label">[B1 EKSİKLİĞİ]</span>
                        <span class="placed-item">Klinik ?</span>
                    </div>

                    <!-- E2 Kofaktör ve İnhibitör -->
                    <div class="drop-zone static-flow" id="slot-lipoikasit" data-accept="LİPOİKASİT">
                        <span class="drop-label">[E2 KOFAKTÖRÜ]</span>
                        <span class="placed-item">?</span>
                    </div>
                    <div class="drop-zone static-flow inhibitor-zone" id="slot-arsenik" data-accept="ARSENİK">
                        <span class="drop-label">[E2 ŞELASYONU / TOKSİN]</span>
                        <span class="placed-item">İnhibitör ?</span>
                    </div>

                    <!-- E3 Kofaktör -->
                    <div class="drop-zone static-flow" id="slot-fad" data-accept="FAD">
                        <span class="drop-label">[E3 KOFAKTÖRÜ (B2)]</span>
                        <span class="placed-item">?</span>
                    </div>
                </div>
            </div>

            <!-- Dairesel Krebs Döngüsü Sahnesi -->
            <div class="krebs-cycle-stage" id="cycle-stage">

                <svg class="cycle-svg" viewBox="0 0 700 610">
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
                    <circle cx="350" cy="305" r="215" fill="none" stroke="url(#orbit-gradient)" stroke-width="3" stroke-dasharray="8 6" />
                    <!-- Akış Okları -->
                    <path d="M 350 90 A 215 215 0 0 1 565 305" fill="none" stroke="#38bdf8" stroke-width="3" marker-end="url(#arrow)"/>
                    <path d="M 565 305 A 215 215 0 0 1 350 520" fill="none" stroke="#38bdf8" stroke-width="3" marker-end="url(#arrow)"/>
                    <path d="M 350 520 A 215 215 0 0 1 135 305" fill="none" stroke="#38bdf8" stroke-width="3" marker-end="url(#arrow)"/>
                    <path d="M 135 305 A 215 215 0 0 1 350 90" fill="none" stroke="#38bdf8" stroke-width="3" marker-end="url(#arrow)"/>
                </svg>

                <!-- Merkez Rozeti -->
                <div class="cycle-center-badge">
                    <i class="fa-solid fa-atom" style="font-size:22px; color:#38bdf8; margin-bottom:3px;"></i>
                    <h3>SİTRİK ASİT SİKLUSU</h3>
                    <span>1 Tur = 10 ATP</span>
                    <span style="color:#94a3b8; font-size:9px;">(3 NADH, 1 FADH2, 1 GTP)</span>
                </div>

                <!-- 1. SİTRAT -->
                <div class="drop-zone" id="slot-sitrat" data-accept="SİTRAT" style="top:40px; right:150px;">
                    <span class="drop-label">1. BASAMAK (6C)</span>
                    <span class="placed-item">?</span>
                </div>

                <!-- İNHİBİTÖR: FLOROASETAT (Akonitaz Bloker) -->
                <div class="drop-zone inhibitor-zone" id="slot-floroasetat" data-accept="FLOROASETAT" style="top:110px; right:12px; min-width:105px;">
                    <span class="drop-label">[ÖLÜMCÜL SENTEZ]</span>
                    <span class="placed-item">İnhibitör ?</span>
                </div>

                <!-- 2. İZOSİTRAT -->
                <div class="drop-zone" id="slot-izositrat" data-accept="İZOSİTRAT" style="top:205px; right:40px;">
                    <span class="drop-label">2. BASAMAK (6C)</span>
                    <span class="placed-item">?</span>
                </div>

                <!-- 3. ALFA-KETOGLUTARAT (Sabit Kılavuz Düğüm) -->
                <div class="fixed-node" style="position:absolute; bottom:185px; right:40px; min-width:115px; border-color:#38bdf8;">
                    <span class="drop-label" style="color:#38bdf8;">3. BASAMAK (5C)</span>
                    <strong style="font-size:11.5px;">α-Ketoglutarat</strong>
                </div>

                <!-- 4. SÜKSİNİL-KoA -->
                <div class="drop-zone" id="slot-suksinilkoa" data-accept="SÜKSİNİLKOA" style="bottom:70px; right:140px;">
                    <span class="drop-label">4. BASAMAK (TİYOESTER)</span>
                    <span class="placed-item">?</span>
                </div>

                <!-- 5. SÜKSİNAT -->
                <div class="drop-zone" id="slot-suksinat" data-accept="SÜKSİNAT" style="bottom:18px; left:50%; transform:translateX(-50%);">
                    <span class="drop-label">5. BASAMAK (GTP ÜRETİMİ)</span>
                    <span class="placed-item">?</span>
                </div>

                <!-- İNHİBİTÖR: MALONAT (Kompleks II Bloker) -->
                <div class="drop-zone inhibitor-zone" id="slot-malonat" data-accept="MALONAT" style="bottom:85px; left:20px; min-width:100px;">
                    <span class="drop-label">[KOMPETİTİF İNH.]</span>
                    <span class="placed-item">İnhibitör ?</span>
                </div>

                <!-- 6. FUMARAT -->
                <div class="drop-zone" id="slot-fumarat" data-accept="FUMARAT" style="bottom:175px; left:75px;">
                    <span class="drop-label">6. BASAMAK (FADH2)</span>
                    <span class="placed-item">?</span>
                </div>

                <!-- 7. MALAT -->
                <div class="drop-zone" id="slot-malat" data-accept="MALAT" style="top:225px; left:45px;">
                    <span class="drop-label">7. BASAMAK (HİDRASYON)</span>
                    <span class="placed-item">?</span>
                </div>

                <!-- 8. OKSALOASETAT -->
                <div class="drop-zone" id="slot-oksaloasetat" data-accept="OKSALOASETAT" style="top:50px; left:140px;">
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
        <i class="fa-solid fa-trophy" style="font-size: 52px; color:#fbbf24; margin-bottom:12px;"></i>
        <h2>Tebrikler Hekim Adayı!</h2>
        <p style="color:#cbd5e1; font-size:13.5px; line-height:1.6;">
            Krebs döngüsü ve PDH köprüsündeki 17 terimin tamamını (metabolitler, 5 kofaktör, KoA, NADH ve klinik blokajları) eksiksiz bulup şemaya yerleştirdiniz!
        </p>
        <button class="restart-btn" onclick="location.reload();">Tekrar Çöz</button>
    </div>
</div>

<script>
/* =========================================================================
1. HARF MATRİSİ VE GİZLİ KELİME VERİLERİ (YATAY & DİKEY DÜZEN - 17 KELİME)
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

// Aranan 17 Kelime Kataloğu (Hepsinin Şemada Birebir Karşılığı Vardır)
const WORDS_TO_FIND = [
    // DİKEYLER (9 Adet)
    { word: "OKSALOASETAT", dir: "vert", r1:0, c1:0, r2:11, c2:0, found: false, placed: false, role: "cycle" },
    { word: "KOENZİMA",     dir: "vert", r1:3, c1:1, r2:10, c2:1, found: false, placed: false, role: "pdh" },
    { word: "İZOSİTRAT",    dir: "vert", r1:1, c1:2, r2:9,  c2:2, found: false, placed: false, role: "cycle" },
    { word: "SÜKSİNAT",     dir: "vert", r1:3, c1:4, r2:10, c2:4, found: false, placed: false, role: "cycle" },
    { word: "SÜKSİNİLKOA",  dir: "vert", r1:2, c1:6, r2:12, c2:6, found: false, placed: false, role: "cycle" },
    { word: "FLOROASETAT",  dir: "vert", r1:0, c1:8, r2:10, c2:8, found: false, placed: false, role: "inhibitor" },
    { word: "FUMARAT",      dir: "vert", r1:2, c1:10,r2:8,  c2:10,found: false, placed: false, role: "cycle" },
    { word: "BERİBERİ",     dir: "vert", r1:3, c1:11,r2:10, c2:11,found: false, placed: false, role: "clinical" },
    { word: "MALAT",        dir: "vert", r1:6, c1:12,r2:10, c2:12,found: false, placed: false, role: "cycle" },
    // YATAYLAR (8 Adet)
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
let selectedTokenForPlacement = null;

/* =========================================================================
2. MATRİS VE KELİME BANKASI OLUŞTURMA
========================================================================= */
const table = document.getElementById("wordsearch-table");
const chipsContainer = document.getElementById("word-bank-chips");
const tokensTray = document.getElementById("tokens-tray");

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

WORDS_TO_FIND.forEach(w => {
    const chip = document.createElement("span");
    chip.className = "word-chip";
    chip.id = `chip-${w.word}`;
    chip.innerHTML = `${w.dir === 'vert' ? '<i class="fa-solid fa-arrow-down"></i>' : '<i class="fa-solid fa-arrow-right"></i>'} ${w.word}`;
    chipsContainer.appendChild(chip);
});

/* =========================================================================
3. SEÇİM MANTIĞI: HEM FARE (MOUSE) HEM DOKUNMATİK (TOUCH)
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
        const letters = selectedCells.map(td => td.innerText).join("");
        const revLetters = letters.split("").reverse().join("");

        let match = WORDS_TO_FIND.find(w => !w.found && (w.word === letters || w.word === revLetters));

        if (match) {
            match.found = true;
            foundWordsCount++;
            document.getElementById("word-score").innerText = `${foundWordsCount} / ${WORDS_TO_FIND.length} Bulundu`;

            selectedCells.forEach(td => {
                if (td.classList.contains("found-vert") || td.classList.contains("found-horiz")) {
                    td.classList.remove("found-vert", "found-horiz");
                    td.classList.add("found-cross");
                } else {
                    td.classList.add(match.dir === "vert" ? "found-vert" : "found-horiz");
                }
            });

            const chip = document.getElementById(`chip-${match.word}`);
            if (chip) chip.classList.add("found");

            createDraggableToken(match);

            showToast(`Harika! "${match.word}" bulundu. Şimdi sağdaki şemada uygun kutucuğa yerleştirin.`, "#38bdf8");
            playSuccessSound();
        }
    }
    clearSelectionStyles();
}

function clearSelectionStyles() {
    const allSelecting = table.querySelectorAll(".selecting");
    allSelecting.forEach(td => td.classList.remove("selecting"));
}

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
    if (tokensTray.querySelector("span")) {
        tokensTray.innerHTML = "";
    }

    const token = document.createElement("div");
    token.className = `drag-token ${match.role}`;
    token.id = `token-${match.word}`;
    token.draggable = true;
    token.innerHTML = `<i class="fa-solid fa-cube"></i> ${match.word}`;
    token.dataset.word = match.word;

    token.addEventListener("dragstart", (e) => {
        e.dataTransfer.setData("text/plain", match.word);
        token.style.opacity = "0.5";
    });

    token.addEventListener("dragend", () => {
        token.style.opacity = "1";
    });

    token.addEventListener("click", () => {
        document.querySelectorAll(".drag-token").forEach(t => t.style.outline = "none");
        selectedTokenForPlacement = match.word;
        token.style.outline = "2px solid #facc15";
        showToast(`"${match.word}" seçildi. Şimdi yerleştirmek istediğiniz hedef kutucuğa tıklayın.`, "#facc15");
    });

    tokensTray.appendChild(token);
}

const dropZones = document.querySelectorAll(".drop-zone");

dropZones.forEach(zone => {
    zone.addEventListener("dragover", (e) => {
        e.preventDefault();
        zone.classList.add("hovered");
    });

    zone.addEventListener("dragleave", () => {
        zone.classList.remove("hovered");
    });

    zone.addEventListener("drop", (e) => {
        e.preventDefault();
        zone.classList.remove("hovered");
        const droppedWord = e.dataTransfer.getData("text/plain");
        checkAndPlaceToken(zone, droppedWord);
    });

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
        zone.classList.add("correct");
        zone.querySelector(".placed-item").innerText = word;

        const tokenElem = document.getElementById(`token-${word}`);
        if (tokenElem) tokenElem.style.display = "none";

        const chip = document.getElementById(`chip-${word}`);
        if (chip) chip.classList.add("placed");

        placedTokensCount++;
        document.getElementById("drop-score").innerText = `${placedTokensCount} / ${WORDS_TO_FIND.length} Yerleşti`;

        showToast(`Harika! ${word} doğru basamağa başarıyla yerleştirildi.`, "#22c55e");
        playSnapSound();

        if (placedTokensCount >= WORDS_TO_FIND.length) {
            setTimeout(() => {
                document.getElementById("modal-success").classList.add("show");
            }, 500);
        }
    } else {
        zone.style.animation = "shake 0.3s ease";
        setTimeout(() => zone.style.animation = "", 350);
        showToast(`Bu hedef kutucuğu "${word}" için uygun değil. Kofaktör ve basamak ipuçlarını inceleyin!`, "#ef4444");
    }
}

function showToast(msg, color="#38bdf8") {
    const toast = document.getElementById("toast-text");
    toast.style.borderColor = color;
    toast.style.color = color;
    toast.innerText = msg;
}

/* =========================================================================
5. WEB AUDIO API SES GERİ BİLDİRİMİ
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
        osc.frequency.setValueAtTime(523.25, audioCtx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(783.99, audioCtx.currentTime + 0.2);
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
components.html(interactive_app_code, height=1050, scrolling=False)
