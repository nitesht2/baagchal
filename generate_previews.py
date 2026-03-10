import cairosvg
from PIL import Image, ImageDraw, ImageFont
import io
import os

OUT_DIR = "/home/user/Claude/previews"
os.makedirs(OUT_DIR, exist_ok=True)

# ============ VERSION 1: Current Design ============
tiger_v1 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<defs><radialGradient id="tg1" cx="50%" cy="40%" r="50%"><stop offset="0%" stop-color="#e8922d"/><stop offset="100%" stop-color="#b56a10"/></radialGradient></defs>
<ellipse cx="32" cy="33" rx="26" ry="27" fill="url(#tg1)"/>
<ellipse cx="12" cy="12" rx="8" ry="10" fill="#d97e1a" transform="rotate(-15 12 12)"/>
<ellipse cx="52" cy="12" rx="8" ry="10" fill="#d97e1a" transform="rotate(15 52 12)"/>
<ellipse cx="12" cy="12" rx="5" ry="7" fill="#ffb366" transform="rotate(-15 12 12)"/>
<ellipse cx="52" cy="12" rx="5" ry="7" fill="#ffb366" transform="rotate(15 52 12)"/>
<ellipse cx="18" cy="38" rx="12" ry="14" fill="#fff8ee" opacity="0.5"/>
<ellipse cx="46" cy="38" rx="12" ry="14" fill="#fff8ee" opacity="0.5"/>
<ellipse cx="32" cy="50" rx="10" ry="7" fill="#fff8ee" opacity="0.45"/>
<ellipse cx="32" cy="42" rx="15" ry="12" fill="#ffe0b0" opacity="0.85"/>
<path d="M22 10 Q24 18 26 24" stroke="#4a2000" stroke-width="4" stroke-linecap="round" fill="none"/>
<path d="M28 8 L30 18" stroke="#4a2000" stroke-width="3" stroke-linecap="round"/>
<path d="M32 7 L32 20" stroke="#4a2000" stroke-width="4.5" stroke-linecap="round"/>
<path d="M36 8 L34 18" stroke="#4a2000" stroke-width="3" stroke-linecap="round"/>
<path d="M42 10 Q40 18 38 24" stroke="#4a2000" stroke-width="4" stroke-linecap="round" fill="none"/>
<path d="M10 24 Q7 30 5 36" stroke="#4a2000" stroke-width="3" stroke-linecap="round" fill="none"/>
<path d="M12 27 Q9 33 8 38" stroke="#4a2000" stroke-width="2.5" stroke-linecap="round" fill="none"/>
<path d="M54 24 Q57 30 59 36" stroke="#4a2000" stroke-width="3" stroke-linecap="round" fill="none"/>
<path d="M52 27 Q55 33 56 38" stroke="#4a2000" stroke-width="2.5" stroke-linecap="round" fill="none"/>
<path d="M15 28 Q22 24 29 28 Q22 33 15 28Z" fill="white"/>
<path d="M35 28 Q42 24 49 28 Q42 33 35 28Z" fill="white"/>
<ellipse cx="22" cy="28" rx="4.5" ry="4" fill="#ffd700"/>
<ellipse cx="42" cy="28" rx="4.5" ry="4" fill="#ffd700"/>
<ellipse cx="22" cy="28" rx="2" ry="4" fill="#111"/>
<ellipse cx="42" cy="28" rx="2" ry="4" fill="#111"/>
<circle cx="20.5" cy="26.5" r="1.5" fill="white" opacity="0.9"/>
<circle cx="40.5" cy="26.5" r="1.5" fill="white" opacity="0.9"/>
<path d="M14 24 Q22 21 29 24" stroke="#4a2000" stroke-width="2" stroke-linecap="round" fill="none"/>
<path d="M35 24 Q42 21 50 24" stroke="#4a2000" stroke-width="2" stroke-linecap="round" fill="none"/>
<path d="M26 38 L32 34 L38 38 Q34 42 30 42 Q26 42 26 38Z" fill="#2a1200"/>
<path d="M32 42 L32 46" stroke="#2a1200" stroke-width="2" fill="none"/>
<path d="M26 47 Q29 50 32 48 Q35 50 38 47" stroke="#2a1200" stroke-width="1.5" fill="none"/>
<line x1="20" y1="40" x2="6" y2="37" stroke="#3a1800" stroke-width="1.2" opacity="0.6"/>
<line x1="20" y1="42" x2="5" y2="42" stroke="#3a1800" stroke-width="1.2" opacity="0.6"/>
<line x1="20" y1="44" x2="6" y2="47" stroke="#3a1800" stroke-width="1.2" opacity="0.5"/>
<line x1="44" y1="40" x2="58" y2="37" stroke="#3a1800" stroke-width="1.2" opacity="0.6"/>
<line x1="44" y1="42" x2="59" y2="42" stroke="#3a1800" stroke-width="1.2" opacity="0.6"/>
<line x1="44" y1="44" x2="58" y2="47" stroke="#3a1800" stroke-width="1.2" opacity="0.5"/>
</svg>'''

goat_v1 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<defs><radialGradient id="gg1" cx="50%" cy="45%" r="50%"><stop offset="0%" stop-color="#f0ece4"/><stop offset="100%" stop-color="#c8c0b0"/></radialGradient></defs>
<path d="M22 22 Q18 12 14 4 Q12 -2 8 -2 Q6 0 8 4 Q12 10 16 18 Q18 22 22 22Z" fill="#887766"/>
<path d="M42 22 Q46 12 50 4 Q52 -2 56 -2 Q58 0 56 4 Q52 10 48 18 Q46 22 42 22Z" fill="#887766"/>
<path d="M19 16 Q16 10 13 3" stroke="#aa9988" stroke-width="2.5" fill="none" stroke-linecap="round"/>
<path d="M45 16 Q48 10 51 3" stroke="#aa9988" stroke-width="2.5" fill="none" stroke-linecap="round"/>
<ellipse cx="32" cy="35" rx="22" ry="24" fill="url(#gg1)"/>
<path d="M28 14 Q30 10 32 14 Q34 10 36 14" stroke="#c8c0b0" stroke-width="2" fill="none" opacity="0.4"/>
<path d="M10 26 Q2 22 -2 24 Q0 27 4 28 Q8 29 12 28Z" fill="#e0d0c0"/>
<path d="M54 26 Q62 22 66 24 Q64 27 60 28 Q56 29 52 28Z" fill="#e0d0c0"/>
<path d="M10 26 Q4 24 1 25 Q3 27 6 27.5 Q9 28 11 27Z" fill="#f5c4c4"/>
<path d="M54 26 Q60 24 63 25 Q61 27 58 27.5 Q55 28 53 27Z" fill="#f5c4c4"/>
<ellipse cx="32" cy="38" rx="10" ry="16" fill="#fff8f0" opacity="0.3"/>
<ellipse cx="22" cy="30" rx="6" ry="5" fill="white"/>
<ellipse cx="42" cy="30" rx="6" ry="5" fill="white"/>
<ellipse cx="22" cy="30" rx="4.5" ry="4" fill="#886633"/>
<ellipse cx="42" cy="30" rx="4.5" ry="4" fill="#886633"/>
<rect x="19.5" y="28.5" width="5" height="3" rx="0.5" fill="#332211"/>
<rect x="39.5" y="28.5" width="5" height="3" rx="0.5" fill="#332211"/>
<circle cx="20.5" cy="28.5" r="1.3" fill="white" opacity="0.8"/>
<circle cx="40.5" cy="28.5" r="1.3" fill="white" opacity="0.8"/>
<path d="M28 43 Q27 45 28.5 45.5" stroke="#6a4a3a" stroke-width="1.8" fill="none" stroke-linecap="round"/>
<path d="M36 43 Q37 45 35.5 45.5" stroke="#6a4a3a" stroke-width="1.8" fill="none" stroke-linecap="round"/>
<path d="M28 48 Q32 51 36 48" stroke="#6a4a3a" stroke-width="1.3" fill="none"/>
<path d="M32 46 L32 48" stroke="#6a4a3a" stroke-width="1.2" fill="none"/>
<path d="M28 50 Q26 56 24 62" stroke="#c0b8a8" stroke-width="2.5" stroke-linecap="round" fill="none" opacity="0.7"/>
<path d="M32 51 Q31 58 30 63" stroke="#c0b8a8" stroke-width="3" stroke-linecap="round" fill="none" opacity="0.6"/>
<path d="M36 50 Q38 56 40 62" stroke="#c0b8a8" stroke-width="2.5" stroke-linecap="round" fill="none" opacity="0.7"/>
</svg>'''

# ============ VERSION 2: Full Body Side View ============
tiger_v2 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<defs><linearGradient id="tb2" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#f0a030"/><stop offset="100%" stop-color="#c06800"/></linearGradient></defs>
<ellipse cx="30" cy="36" rx="22" ry="14" fill="url(#tb2)"/>
<circle cx="48" cy="26" r="13" fill="#e89030"/>
<ellipse cx="42" cy="14" rx="4" ry="6" fill="#d07820"/>
<ellipse cx="42" cy="14" rx="2.5" ry="4" fill="#ffb060"/>
<ellipse cx="54" cy="16" rx="4" ry="5" fill="#d07820"/>
<ellipse cx="54" cy="16" rx="2.5" ry="3.5" fill="#ffb060"/>
<path d="M18 26 Q16 36 18 46" stroke="#4a2000" stroke-width="2.5" fill="none" stroke-linecap="round"/>
<path d="M24 24 Q22 36 24 48" stroke="#4a2000" stroke-width="2.5" fill="none" stroke-linecap="round"/>
<path d="M30 23 Q28 36 30 49" stroke="#4a2000" stroke-width="2.5" fill="none" stroke-linecap="round"/>
<path d="M36 24 Q34 34 36 46" stroke="#4a2000" stroke-width="2" fill="none" stroke-linecap="round"/>
<rect x="14" y="46" width="5" height="14" rx="2" fill="#c06800"/>
<rect x="22" y="46" width="5" height="14" rx="2" fill="#d07820"/>
<rect x="33" y="44" width="5" height="16" rx="2" fill="#c06800"/>
<rect x="40" y="43" width="5" height="15" rx="2" fill="#d07820"/>
<path d="M8 32 Q2 28 4 22 Q6 18 8 20" stroke="#e89030" stroke-width="4" fill="none" stroke-linecap="round"/>
<path d="M4 22 Q6 18 8 20" stroke="#4a2000" stroke-width="2" fill="none"/>
<ellipse cx="28" cy="44" rx="16" ry="5" fill="#ffe8cc" opacity="0.5"/>
<ellipse cx="48" cy="30" rx="8" ry="6" fill="#ffe0b0" opacity="0.7"/>
<ellipse cx="52" cy="24" rx="3" ry="2.5" fill="white"/>
<ellipse cx="52.5" cy="24" rx="1.8" ry="2" fill="#ffd700"/>
<ellipse cx="53" cy="24" rx="0.8" ry="2" fill="#111"/>
<circle cx="51.5" cy="23" r="0.8" fill="white" opacity="0.9"/>
<path d="M58 27 L60 25 L62 27 Q61 29 59 29 Q57 29 58 27Z" fill="#2a1200"/>
<path d="M58 30 Q60 32 62 30" stroke="#2a1200" stroke-width="1" fill="none"/>
<line x1="58" y1="28" x2="64" y2="26" stroke="#4a2000" stroke-width="0.8" opacity="0.5"/>
<line x1="58" y1="29" x2="64" y2="29" stroke="#4a2000" stroke-width="0.8" opacity="0.5"/>
<path d="M44 18 Q46 14 48 18" stroke="#4a2000" stroke-width="2" fill="none" stroke-linecap="round"/>
<path d="M48 16 L49 20" stroke="#4a2000" stroke-width="2" stroke-linecap="round"/>
<path d="M52 18 Q54 14 56 18" stroke="#4a2000" stroke-width="1.5" fill="none" stroke-linecap="round"/>
</svg>'''

goat_v2 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<defs><linearGradient id="gb2" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#f0ece4"/><stop offset="100%" stop-color="#c8c0b0"/></linearGradient></defs>
<ellipse cx="30" cy="34" rx="20" ry="12" fill="url(#gb2)"/>
<ellipse cx="50" cy="24" rx="10" ry="11" fill="#e8e0d4"/>
<path d="M46 14 Q44 6 40 2 Q38 0 40 4 Q42 8 44 14" stroke="#887766" stroke-width="3" fill="none" stroke-linecap="round"/>
<path d="M54 14 Q56 6 58 2 Q60 -1 58 4 Q56 8 54 14" stroke="#887766" stroke-width="3" fill="none" stroke-linecap="round"/>
<path d="M42 18 Q36 14 34 18 Q38 19 42 20" fill="#e0d0c0"/>
<path d="M42 18 Q38 16 36 18 Q38 19 41 19.5" fill="#f5c4c4"/>
<rect x="16" y="42" width="4" height="16" rx="1.5" fill="#c8c0b0"/>
<rect x="23" y="42" width="4" height="16" rx="1.5" fill="#d8d0c4"/>
<rect x="34" y="41" width="4" height="17" rx="1.5" fill="#c8c0b0"/>
<rect x="40" y="40" width="4" height="16" rx="1.5" fill="#d8d0c4"/>
<rect x="15" y="56" width="6" height="4" rx="1" fill="#555"/>
<rect x="22" y="56" width="6" height="4" rx="1" fill="#555"/>
<rect x="33" y="56" width="6" height="4" rx="1" fill="#555"/>
<rect x="39" y="54" width="6" height="4" rx="1" fill="#555"/>
<path d="M10 30 Q6 26 8 22" stroke="#c8c0b0" stroke-width="3" fill="none" stroke-linecap="round"/>
<ellipse cx="28" cy="42" rx="14" ry="4" fill="white" opacity="0.3"/>
<ellipse cx="54" cy="22" rx="3" ry="2.5" fill="white"/>
<ellipse cx="54" cy="22" rx="2.2" ry="2" fill="#886633"/>
<rect x="53" y="21" width="3" height="2" rx="0.3" fill="#332211"/>
<circle cx="53" cy="21" r="0.8" fill="white" opacity="0.8"/>
<ellipse cx="59" cy="27" rx="2" ry="1.5" fill="#6a4a3a"/>
<path d="M56 30 Q58 32 60 30" stroke="#6a4a3a" stroke-width="1" fill="none"/>
<path d="M54 32 Q52 38 50 42" stroke="#c0b8a8" stroke-width="2" fill="none" opacity="0.6" stroke-linecap="round"/>
<path d="M56 33 Q54 38 53 42" stroke="#c0b8a8" stroke-width="2.5" fill="none" opacity="0.5" stroke-linecap="round"/>
</svg>'''

# ============ VERSION 3: Bold Minimalist ============
tiger_v3 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<circle cx="32" cy="34" r="26" fill="#e88020"/>
<circle cx="14" cy="14" r="8" fill="#d07020"/>
<circle cx="50" cy="14" r="8" fill="#d07020"/>
<circle cx="14" cy="14" r="5" fill="#ffb060"/>
<circle cx="50" cy="14" r="5" fill="#ffb060"/>
<path d="M16 18 L14 32" stroke="#3a1500" stroke-width="5" stroke-linecap="round"/>
<path d="M24 14 L22 30" stroke="#3a1500" stroke-width="5" stroke-linecap="round"/>
<path d="M32 12 L32 28" stroke="#3a1500" stroke-width="5" stroke-linecap="round"/>
<path d="M40 14 L42 30" stroke="#3a1500" stroke-width="5" stroke-linecap="round"/>
<path d="M48 18 L50 32" stroke="#3a1500" stroke-width="5" stroke-linecap="round"/>
<ellipse cx="32" cy="44" rx="14" ry="10" fill="#fff0dd"/>
<ellipse cx="22" cy="32" rx="5" ry="3.5" fill="white"/>
<ellipse cx="42" cy="32" rx="5" ry="3.5" fill="white"/>
<ellipse cx="23" cy="32" rx="2.5" ry="3.5" fill="#111"/>
<ellipse cx="43" cy="32" rx="2.5" ry="3.5" fill="#111"/>
<circle cx="21.5" cy="30.5" r="1.2" fill="white"/>
<circle cx="41.5" cy="30.5" r="1.2" fill="white"/>
<path d="M28 41 L32 38 L36 41 Z" fill="#2a1200"/>
<path d="M32 41 L32 44" stroke="#2a1200" stroke-width="1.5"/>
<path d="M28 45 Q32 48 36 45" stroke="#2a1200" stroke-width="1.5" fill="none"/>
</svg>'''

goat_v3 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<circle cx="32" cy="36" r="24" fill="#e8e0d4"/>
<path d="M24 16 Q20 4 14 -2" stroke="#776655" stroke-width="5" fill="none" stroke-linecap="round"/>
<path d="M40 16 Q44 4 50 -2" stroke="#776655" stroke-width="5" fill="none" stroke-linecap="round"/>
<path d="M23 14 Q19 4 14 -1" stroke="#aa9977" stroke-width="2" fill="none" stroke-linecap="round"/>
<path d="M41 14 Q45 4 50 -1" stroke="#aa9977" stroke-width="2" fill="none" stroke-linecap="round"/>
<ellipse cx="10" cy="28" rx="8" ry="4" fill="#d8c8b8" transform="rotate(-10 10 28)"/>
<ellipse cx="54" cy="28" rx="8" ry="4" fill="#d8c8b8" transform="rotate(10 54 28)"/>
<ellipse cx="32" cy="38" rx="8" ry="14" fill="white" opacity="0.4"/>
<circle cx="22" cy="32" r="4.5" fill="white"/>
<circle cx="42" cy="32" r="4.5" fill="white"/>
<circle cx="22" cy="32" r="3.2" fill="#886633"/>
<circle cx="42" cy="32" r="3.2" fill="#886633"/>
<rect x="19.5" y="31" width="5" height="2.5" rx="0.3" fill="#222"/>
<rect x="39.5" y="31" width="5" height="2.5" rx="0.3" fill="#222"/>
<circle cx="21" cy="30.5" r="1" fill="white"/>
<circle cx="41" cy="30.5" r="1" fill="white"/>
<ellipse cx="32" cy="44" rx="4" ry="2.5" fill="#8a6a5a"/>
<path d="M29 48 Q32 51 35 48" stroke="#6a4a3a" stroke-width="1.5" fill="none"/>
<path d="M28 52 Q26 58 24 62" stroke="#b0a898" stroke-width="3" fill="none" stroke-linecap="round" opacity="0.7"/>
<path d="M32 53 L32 63" stroke="#b0a898" stroke-width="3.5" fill="none" stroke-linecap="round" opacity="0.6"/>
<path d="M36 52 Q38 58 40 62" stroke="#b0a898" stroke-width="3" fill="none" stroke-linecap="round" opacity="0.7"/>
</svg>'''

# ============ VERSION 4: Cute Cartoon ============
tiger_v4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<defs><radialGradient id="tc4" cx="50%" cy="40%" r="50%"><stop offset="0%" stop-color="#ffaa44"/><stop offset="100%" stop-color="#dd7700"/></radialGradient></defs>
<circle cx="32" cy="34" r="28" fill="url(#tc4)"/>
<circle cx="10" cy="12" r="9" fill="#dd7700"/>
<circle cx="54" cy="12" r="9" fill="#dd7700"/>
<circle cx="10" cy="12" r="5.5" fill="#ffcc88"/>
<circle cx="54" cy="12" r="5.5" fill="#ffcc88"/>
<ellipse cx="20" cy="42" rx="11" ry="10" fill="white" opacity="0.85"/>
<ellipse cx="44" cy="42" rx="11" ry="10" fill="white" opacity="0.85"/>
<path d="M18 12 L16 22" stroke="#552200" stroke-width="3.5" stroke-linecap="round"/>
<path d="M26 10 L25 20" stroke="#552200" stroke-width="3.5" stroke-linecap="round"/>
<path d="M32 8 L32 18" stroke="#552200" stroke-width="4" stroke-linecap="round"/>
<path d="M38 10 L39 20" stroke="#552200" stroke-width="3.5" stroke-linecap="round"/>
<path d="M46 12 L48 22" stroke="#552200" stroke-width="3.5" stroke-linecap="round"/>
<path d="M6 28 L10 26" stroke="#552200" stroke-width="2.5" stroke-linecap="round"/>
<path d="M5 34 L10 33" stroke="#552200" stroke-width="2.5" stroke-linecap="round"/>
<path d="M58 28 L54 26" stroke="#552200" stroke-width="2.5" stroke-linecap="round"/>
<path d="M59 34 L54 33" stroke="#552200" stroke-width="2.5" stroke-linecap="round"/>
<ellipse cx="22" cy="30" rx="7" ry="7.5" fill="white"/>
<ellipse cx="42" cy="30" rx="7" ry="7.5" fill="white"/>
<ellipse cx="23" cy="31" rx="5" ry="5.5" fill="#333"/>
<ellipse cx="43" cy="31" rx="5" ry="5.5" fill="#333"/>
<circle cx="21" cy="28.5" r="2.5" fill="white"/>
<circle cx="41" cy="28.5" r="2.5" fill="white"/>
<circle cx="25" cy="32" r="1.2" fill="white" opacity="0.6"/>
<circle cx="45" cy="32" r="1.2" fill="white" opacity="0.6"/>
<path d="M28 40 L32 36 L36 40 Z" fill="#ff6688"/>
<path d="M24 44 Q28 48 32 44 Q36 48 40 44" stroke="#552200" stroke-width="1.8" fill="none" stroke-linecap="round"/>
<ellipse cx="14" cy="40" rx="4" ry="2.5" fill="#ff8888" opacity="0.3"/>
<ellipse cx="50" cy="40" rx="4" ry="2.5" fill="#ff8888" opacity="0.3"/>
</svg>'''

goat_v4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<defs><radialGradient id="gc4" cx="50%" cy="45%" r="50%"><stop offset="0%" stop-color="#fff8f0"/><stop offset="100%" stop-color="#ddd4c8"/></radialGradient></defs>
<circle cx="32" cy="36" r="26" fill="url(#gc4)"/>
<path d="M22 14 Q16 2 10 -4" stroke="#998877" stroke-width="5" fill="none" stroke-linecap="round"/>
<path d="M42 14 Q48 2 54 -4" stroke="#998877" stroke-width="5" fill="none" stroke-linecap="round"/>
<path d="M21 13 Q16 3 11 -3" stroke="#bbaa99" stroke-width="2.5" fill="none" stroke-linecap="round"/>
<path d="M43 13 Q48 3 53 -3" stroke="#bbaa99" stroke-width="2.5" fill="none" stroke-linecap="round"/>
<circle cx="26" cy="14" r="6" fill="#f0ece4"/>
<circle cx="32" cy="12" r="7" fill="#f0ece4"/>
<circle cx="38" cy="14" r="6" fill="#f0ece4"/>
<ellipse cx="6" cy="28" rx="9" ry="5" fill="#e0d0c0" transform="rotate(-15 6 28)"/>
<ellipse cx="58" cy="28" rx="9" ry="5" fill="#e0d0c0" transform="rotate(15 58 28)"/>
<ellipse cx="6" cy="28" rx="6" ry="3" fill="#f5c4c4" transform="rotate(-15 6 28)"/>
<ellipse cx="58" cy="28" rx="6" ry="3" fill="#f5c4c4" transform="rotate(15 58 28)"/>
<ellipse cx="22" cy="32" rx="7" ry="7.5" fill="white"/>
<ellipse cx="42" cy="32" rx="7" ry="7.5" fill="white"/>
<ellipse cx="23" cy="33" rx="4.5" ry="5" fill="#664422"/>
<ellipse cx="43" cy="33" rx="4.5" ry="5" fill="#664422"/>
<rect x="20.5" y="31.5" width="5" height="2.5" rx="0.3" fill="#222"/>
<rect x="40.5" y="31.5" width="5" height="2.5" rx="0.3" fill="#222"/>
<circle cx="21" cy="30.5" r="2.2" fill="white"/>
<circle cx="41" cy="30.5" r="2.2" fill="white"/>
<circle cx="25" cy="34" r="1" fill="white" opacity="0.5"/>
<circle cx="45" cy="34" r="1" fill="white" opacity="0.5"/>
<ellipse cx="32" cy="44" rx="4" ry="3" fill="#dda0a0"/>
<ellipse cx="30" cy="44.5" rx="1" ry="0.8" fill="#aa7070"/>
<ellipse cx="34" cy="44.5" rx="1" ry="0.8" fill="#aa7070"/>
<path d="M28 48 Q32 52 36 48" stroke="#886655" stroke-width="1.5" fill="none" stroke-linecap="round"/>
<ellipse cx="14" cy="40" rx="4" ry="2.5" fill="#ffaaaa" opacity="0.3"/>
<ellipse cx="50" cy="40" rx="4" ry="2.5" fill="#ffaaaa" opacity="0.3"/>
<path d="M29 52 Q27 58 26 63" stroke="#c8c0b0" stroke-width="2.5" fill="none" stroke-linecap="round" opacity="0.6"/>
<path d="M32 53 Q32 59 32 64" stroke="#c8c0b0" stroke-width="3" fill="none" stroke-linecap="round" opacity="0.5"/>
<path d="M35 52 Q37 58 38 63" stroke="#c8c0b0" stroke-width="2.5" fill="none" stroke-linecap="round" opacity="0.6"/>
</svg>'''

# ============ VERSION 5: Fierce & Realistic ============
tiger_v5 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<defs><radialGradient id="tr5" cx="50%" cy="40%" r="55%"><stop offset="0%" stop-color="#f0a030"/><stop offset="60%" stop-color="#cc7010"/><stop offset="100%" stop-color="#884400"/></radialGradient></defs>
<ellipse cx="32" cy="34" rx="28" ry="28" fill="url(#tr5)"/>
<path d="M8 8 Q12 2 18 8 Q14 6 10 10 Z" fill="#aa5500"/>
<path d="M56 8 Q52 2 46 8 Q50 6 54 10 Z" fill="#aa5500"/>
<path d="M10 8 Q13 4 16 8" fill="#ffbb66"/>
<path d="M54 8 Q51 4 48 8" fill="#ffbb66"/>
<ellipse cx="16" cy="42" rx="13" ry="14" fill="#fff4e0" opacity="0.65"/>
<ellipse cx="48" cy="42" rx="13" ry="14" fill="#fff4e0" opacity="0.65"/>
<ellipse cx="32" cy="52" rx="12" ry="8" fill="#fff4e0" opacity="0.5"/>
<path d="M20 8 Q22 16 24 24" stroke="#3a1500" stroke-width="4.5" stroke-linecap="round" fill="none"/>
<path d="M27 6 L28 18" stroke="#3a1500" stroke-width="3.5" stroke-linecap="round"/>
<path d="M32 5 L32 20" stroke="#3a1500" stroke-width="5" stroke-linecap="round"/>
<path d="M37 6 L36 18" stroke="#3a1500" stroke-width="3.5" stroke-linecap="round"/>
<path d="M44 8 Q42 16 40 24" stroke="#3a1500" stroke-width="4.5" stroke-linecap="round" fill="none"/>
<path d="M8 22 Q4 30 3 38" stroke="#3a1500" stroke-width="3.5" stroke-linecap="round" fill="none"/>
<path d="M11 26 Q8 32 7 40" stroke="#3a1500" stroke-width="2.5" stroke-linecap="round" fill="none"/>
<path d="M14 28 Q12 34 11 40" stroke="#3a1500" stroke-width="2" stroke-linecap="round" fill="none" opacity="0.7"/>
<path d="M56 22 Q60 30 61 38" stroke="#3a1500" stroke-width="3.5" stroke-linecap="round" fill="none"/>
<path d="M53 26 Q56 32 57 40" stroke="#3a1500" stroke-width="2.5" stroke-linecap="round" fill="none"/>
<path d="M50 28 Q52 34 53 40" stroke="#3a1500" stroke-width="2" stroke-linecap="round" fill="none" opacity="0.7"/>
<ellipse cx="32" cy="42" rx="13" ry="10" fill="#ffe4c0" opacity="0.9"/>
<path d="M14 28 Q22 23 30 28 Q22 34 14 28Z" fill="white"/>
<path d="M34 28 Q42 23 50 28 Q42 34 34 28Z" fill="white"/>
<ellipse cx="22" cy="28" rx="5" ry="4" fill="#e6aa00"/>
<ellipse cx="42" cy="28" rx="5" ry="4" fill="#e6aa00"/>
<ellipse cx="22" cy="28" rx="2.2" ry="4" fill="#111"/>
<ellipse cx="42" cy="28" rx="2.2" ry="4" fill="#111"/>
<circle cx="20.5" cy="26.5" r="1.8" fill="white" opacity="0.9"/>
<circle cx="40.5" cy="26.5" r="1.8" fill="white" opacity="0.9"/>
<path d="M13 24 Q22 20 30 24" stroke="#3a1500" stroke-width="2.5" stroke-linecap="round" fill="none"/>
<path d="M34 24 Q42 20 51 24" stroke="#3a1500" stroke-width="2.5" stroke-linecap="round" fill="none"/>
<path d="M25 38 L32 33 L39 38 Q36 43 32 43 Q28 43 25 38Z" fill="#2a1200"/>
<path d="M32 43 L32 47" stroke="#2a1200" stroke-width="2" fill="none"/>
<path d="M25 48 Q28 52 32 49 Q36 52 39 48" stroke="#2a1200" stroke-width="2" fill="none" stroke-linecap="round"/>
<line x1="18" y1="40" x2="2" y2="36" stroke="#3a1800" stroke-width="1.5" opacity="0.5"/>
<line x1="18" y1="42" x2="1" y2="42" stroke="#3a1800" stroke-width="1.5" opacity="0.5"/>
<line x1="18" y1="44" x2="2" y2="48" stroke="#3a1800" stroke-width="1.3" opacity="0.4"/>
<line x1="46" y1="40" x2="62" y2="36" stroke="#3a1800" stroke-width="1.5" opacity="0.5"/>
<line x1="46" y1="42" x2="63" y2="42" stroke="#3a1800" stroke-width="1.5" opacity="0.5"/>
<line x1="46" y1="44" x2="62" y2="48" stroke="#3a1800" stroke-width="1.3" opacity="0.4"/>
</svg>'''

goat_v5 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<defs><radialGradient id="gr5" cx="50%" cy="40%" r="55%"><stop offset="0%" stop-color="#f4efe8"/><stop offset="60%" stop-color="#d4ccc0"/><stop offset="100%" stop-color="#a09888"/></radialGradient></defs>
<ellipse cx="32" cy="36" rx="24" ry="26" fill="url(#gr5)"/>
<path d="M22 18 Q16 8 10 0 Q6 -6 4 -4 Q2 -2 6 2 Q10 8 14 16 Q18 22 22 22Z" fill="#887766"/>
<path d="M42 18 Q48 8 54 0 Q58 -6 60 -4 Q62 -2 58 2 Q54 8 50 16 Q46 22 42 22Z" fill="#887766"/>
<path d="M18 14 Q14 6 10 0" stroke="#bbaa99" stroke-width="2.5" fill="none" stroke-linecap="round"/>
<path d="M16 10 Q13 4 9 -2" stroke="#ccbbaa" stroke-width="1.5" fill="none" stroke-linecap="round" opacity="0.6"/>
<path d="M46 14 Q50 6 54 0" stroke="#bbaa99" stroke-width="2.5" fill="none" stroke-linecap="round"/>
<path d="M48 10 Q51 4 55 -2" stroke="#ccbbaa" stroke-width="1.5" fill="none" stroke-linecap="round" opacity="0.6"/>
<path d="M26 14 Q28 10 30 14" stroke="#d4ccc0" stroke-width="2" fill="none"/>
<path d="M30 12 Q32 8 34 12" stroke="#d4ccc0" stroke-width="2.5" fill="none"/>
<path d="M34 14 Q36 10 38 14" stroke="#d4ccc0" stroke-width="2" fill="none"/>
<path d="M8 26 Q0 20 -4 22 Q-2 26 2 28 Q6 29 10 28Z" fill="#d8c8b8"/>
<path d="M56 26 Q64 20 68 22 Q66 26 62 28 Q58 29 54 28Z" fill="#d8c8b8"/>
<path d="M8 26 Q2 22 -1 24 Q1 26 4 27 Q7 28 9 27Z" fill="#eec0b8"/>
<path d="M56 26 Q62 22 65 24 Q63 26 60 27 Q57 28 55 27Z" fill="#eec0b8"/>
<path d="M26 20 Q32 18 38 20 L38 52 Q32 54 26 52 Z" fill="white" opacity="0.25"/>
<ellipse cx="20" cy="30" rx="6.5" ry="5.5" fill="white"/>
<ellipse cx="44" cy="30" rx="6.5" ry="5.5" fill="white"/>
<ellipse cx="20" cy="30" rx="5" ry="4.5" fill="#aa7733"/>
<ellipse cx="44" cy="30" rx="5" ry="4.5" fill="#aa7733"/>
<rect x="17" y="28.5" width="6" height="3" rx="0.5" fill="#221100"/>
<rect x="41" y="28.5" width="6" height="3" rx="0.5" fill="#221100"/>
<circle cx="18.5" cy="28" r="1.5" fill="white" opacity="0.85"/>
<circle cx="42.5" cy="28" r="1.5" fill="white" opacity="0.85"/>
<ellipse cx="32" cy="46" rx="10" ry="8" fill="#e4dcd4" opacity="0.7"/>
<path d="M27 44 Q25.5 46.5 27.5 47" stroke="#6a4a3a" stroke-width="2" fill="none" stroke-linecap="round"/>
<path d="M37 44 Q38.5 46.5 36.5 47" stroke="#6a4a3a" stroke-width="2" fill="none" stroke-linecap="round"/>
<path d="M32 48 L32 50" stroke="#5a3a2a" stroke-width="1.5" fill="none"/>
<path d="M27 51 Q30 53 32 51 Q34 53 37 51" stroke="#5a3a2a" stroke-width="1.5" fill="none" stroke-linecap="round"/>
<path d="M26 52 Q24 58 22 63" stroke="#b8b0a0" stroke-width="2.5" fill="none" stroke-linecap="round" opacity="0.7"/>
<path d="M29 53 Q27 59 26 64" stroke="#b8b0a0" stroke-width="2" fill="none" stroke-linecap="round" opacity="0.5"/>
<path d="M32 54 Q31 60 30 64" stroke="#b8b0a0" stroke-width="3" fill="none" stroke-linecap="round" opacity="0.6"/>
<path d="M35 53 Q37 59 38 64" stroke="#b8b0a0" stroke-width="2" fill="none" stroke-linecap="round" opacity="0.5"/>
<path d="M38 52 Q40 58 42 63" stroke="#b8b0a0" stroke-width="2.5" fill="none" stroke-linecap="round" opacity="0.7"/>
</svg>'''

# Render all versions
versions = [
    ("V1 Current", tiger_v1, goat_v1),
    ("V2 Full Body", tiger_v2, goat_v2),
    ("V3 Minimalist", tiger_v3, goat_v3),
    ("V4 Cute Cartoon", tiger_v4, goat_v4),
    ("V5 Fierce Realistic", tiger_v5, goat_v5),
]

SIZE = 200  # render size for each piece

for name, tiger_svg, goat_svg in versions:
    fname = name.replace(" ", "_").lower()

    # Render tiger
    tiger_png = cairosvg.svg2png(bytestring=tiger_svg.encode(), output_width=SIZE, output_height=SIZE)
    tiger_img = Image.open(io.BytesIO(tiger_png)).convert("RGBA")

    # Render goat
    goat_png = cairosvg.svg2png(bytestring=goat_svg.encode(), output_width=SIZE, output_height=SIZE)
    goat_img = Image.open(io.BytesIO(goat_png)).convert("RGBA")

    # Create combined image with dark background
    combined = Image.new("RGBA", (SIZE * 2 + 60, SIZE + 40), (26, 26, 46, 255))
    combined.paste(tiger_img, (20, 20), tiger_img)
    combined.paste(goat_img, (SIZE + 40, 20), goat_img)

    combined.save(f"{OUT_DIR}/{fname}.png")
    print(f"Saved {fname}.png")

print("All previews generated!")
