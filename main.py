< !DOCTYPE
html >
< html
lang = "en" >
< head >
< meta
charset = "UTF-8" >
< meta
name = "viewport"
content = "width=device-width, initial-scale=1.0" >
< title > All
Things
Are
Designed
III < / title >

< !-- Tailwind
CSS -->
< script
src = "https://cdn.tailwindcss.com" > < / script >

< !-- Babel
for translating JSX in the browser -->
< script
src = "https://unpkg.com/@babel/standalone/babel.min.js" > < / script >

< !-- Import
Map
to
allow
standard
import syntax

- UPDATED
TO
REACT
18.3
.1
TO
FIX
VERSION
CONFLICTS -->
< script
type = "importmap" >
{
    "imports": {
        "react": "https://esm.sh/react@18.3.1",
        "react-dom/client": "https://esm.sh/react-dom@18.3.1/client",
        "lucide-react": "https://esm.sh/lucide-react@0.460.0?deps=react@18.3.1"
    }
}
< / script >

< style >
/ *Custom
scrollbar
for a cleaner look * /
::-webkit - scrollbar
{
    width: 8px;
}
::-webkit - scrollbar - track
{
    background: transparent;
}
::-webkit - scrollbar - thumb
{
    background:  # d1d5db;
        border - radius: 4
px;
}
::-webkit - scrollbar - thumb: hover
{
    background:  # 9ca3af;
}
body
{
    font - family: 'Inter', system - ui, -apple - system, sans - serif;
}
< / style >
< / head >
< body >
< div
id = "root" > < / div >

< !-- Main
Application
Script -->
< script
type = "text/babel"
data - type = "module" >
import React,

{useState, useMemo}
from

'react';
import

{createRoot}
from

'react-dom/client';
import

{Search, Link, Filter, Plus, X, LayoutGrid, LayoutList, Moon, Sun, Sparkles}
from

'lucide-react';

// --- STYLING
CONSTANTS - --

// Helper
to
get
tag
colors
based
on
theme
const
getCategoryColors = (category, isDark) = > {
    const
colors = {
    'All': isDark ? 'text-gray-400 border-gray-600': 'text-gray-600 border-gray-300',
'Discover': isDark ? 'text-amber-300 border-amber-500': 'text-amber-600 border-amber-300',
'Agency & Studio': isDark ? 'text-blue-300 border-blue-800': 'text-blue-600 border-blue-200',
'Typography': isDark ? 'text-pink-300 border-pink-800': 'text-pink-600 border-pink-200',
'Mockups & Assets': isDark ? 'text-green-300 border-green-800': 'text-green-600 border-green-200',
'Publications & Archives': isDark ? 'text-purple-300 border-purple-800': 'text-purple-600 border-purple-200',
'Reading List': isDark ? 'text-yellow-300 border-yellow-800': 'text-yellow-600 border-yellow-200',
'Material & Print': isDark ? 'text-red-300 border-red-800': 'text-red-600 border-red-200',
'Designer Portfolio': isDark ? 'text-indigo-300 border-indigo-800': 'text-indigo-600 border-indigo-200',
'Sound & Audio': isDark ? 'text-teal-300 border-teal-800': 'text-teal-600 border-teal-200',
'Tools': isDark ? 'text-cyan-300 border-cyan-800': 'text-cyan-600 border-cyan-200',
'Theory': isDark ? 'text-orange-300 border-orange-800': 'text-orange-600 border-orange-200',
'Iconography': isDark ? 'text-fuchsia-300 border-fuchsia-800': 'text-fuchsia-600 border-fuchsia-200',
'Logos': isDark ? 'text-violet-300 border-violet-800': 'text-violet-600 border-violet-200',
'Architecture': isDark ? 'text-lime-300 border-lime-800': 'text-lime-600 border-lime-200',
};
return colors[category] | | (isDark ? 'text-gray-400 border-gray-600': 'text-gray-600 border-gray-300');
};

// Helper
for active filter button backgrounds
const getActiveCategoryStyles = (category, isDark) = > {
if (isDark) {
const darkStyles = {
'All': 'bg-gray-800 text-gray-200 border-gray-600',
'Discover': 'bg-amber-900/40 text-amber-200 border-amber-700',
'Agency & Studio': 'bg-blue-900/40 text-blue-200 border-blue-700',
'Typography': 'bg-pink-900/40 text-pink-200 border-pink-700',
'Mockups & Assets': 'bg-green-900/40 text-green-200 border-green-700',
'Publications & Archives': 'bg-purple-900/40 text-purple-200 border-purple-700',
'Reading List': 'bg-yellow-900/40 text-yellow-200 border-yellow-700',
'Material & Print': 'bg-red-900/40 text-red-200 border-red-700',
'Designer Portfolio': 'bg-indigo-900/40 text-indigo-200 border-indigo-700',
'Sound & Audio': 'bg-teal-900/40 text-teal-200 border-teal-700',
'Tools': 'bg-cyan-900/40 text-cyan-200 border-cyan-700',
'Theory': 'bg-orange-900/40 text-orange-200 border-orange-700',
'Iconography': 'bg-fuchsia-900/40 text-fuchsia-200 border-fuchsia-700',
'Logos': 'bg-violet-900/40 text-violet-200 border-violet-700',
'Architecture': 'bg-lime-900/40 text-lime-200 border-lime-700',
};
return darkStyles[category] | | 'bg-gray-800 text-gray-200';
}

// Light
Mode
Styles
const
lightStyles = {
'All': 'bg-gray-200/80 border-gray-300 text-gray-800',
'Discover': 'bg-amber-100/80 border-amber-200 text-amber-700',
'Agency & Studio': 'bg-blue-100/50 border-blue-200 text-blue-700',
'Typography': 'bg-pink-100/50 border-pink-200 text-pink-700',
'Mockups & Assets': 'bg-green-100/50 border-green-200 text-green-700',
'Publications & Archives': 'bg-purple-100/50 border-purple-200 text-purple-700',
'Reading List': 'bg-yellow-100/50 border-yellow-200 text-yellow-700',
'Material & Print': 'bg-red-100/50 border-red-200 text-red-700',
'Designer Portfolio': 'bg-indigo-100/50 border-indigo-200 text-indigo-700',
'Sound & Audio': 'bg-teal-100/50 border-teal-200 text-teal-700',
'Tools': 'bg-cyan-100/50 border-cyan-200 text-cyan-700',
'Theory': 'bg-orange-100/50 border-orange-200 text-orange-700',
'Iconography': 'bg-fuchsia-100/50 border-fuchsia-200 text-fuchsia-700',
'Logos': 'bg-violet-100/50 border-violet-200 text-violet-700',
'Architecture': 'bg-lime-100/50 border-lime-200 text-lime-700',
};
return lightStyles[category] | | 'bg-gray-100 text-gray-800';
};

// --- USER
DATA - --
const
INITIAL_USER_DATA = [
// --- Agency & Studio - --
{id: 101, title: "Integral typography", category: "Agency & Studio",
 description: "French (Paris) based studio focusing on typography-driven graphic design.",
 url: "https://www.integral-typography.eu"},
{id: 102, title: "Universal everything", category: "Agency & Studio",
 description: "Creative studio specializing in 3D and immersive digital experiences.",
 url: "https://www.universaleverything.com"},
{id: 103, title: "Uniteditions", category: "Agency & Studio",
 description: "Shop for high-quality graphic design books and printed matter.", url: "https://www.uniteditions.com"},
{id: 104, title: "Base design (Debailleul work)", category: "Agency & Studio",
 description: "Branding and digital case study with a highly conceptual approach.",
 url: "https://www.basedesign.com/work/debailleul-debailleul"},
{id: 105, title: "HCMA", category: "Agency & Studio",
 description: "Architecture and branding studio (Linktree reference).", url: "https://linktr.ee/hcma.ca"},
{id: 106, title: "Obys agency grids", category: "Agency & Studio",
 description: "Research and examples focusing on grids, digital layouts, and design studies.",
 url: "https://grids.obys.agency"},
{id: 107, title: "Gothamiti", category: "Agency & Studio",
 description: "Digital branding agency with an amazing portfolio of work.", url: "https://www.gothamsiti.it/works"},
{id: 108, title: "Refik Anadol studio", category: "Agency & Studio",
 description: "Studio focused on AI, data sculpture, and 3D media experiences.", url: "https://refikanadolstudio.com"},
{id: 109, title: "Spin studio", category: "Agency & Studio",
 description: "High-quality branding agency portfolio with sophisticated, minimal work.",
 url: "https://spin.co.uk/work"},
{id: 110, title: "The shift Tokyo", category: "Agency & Studio",
 description: "A community and network of design agencies based in Tokyo.", url: "https://theshift.tokyo/en/about"},
{id: 111, title: "Studio banana", category: "Agency & Studio",
 description: "Innovative and multicultural design studio.", url: "https://studiobanana.com"},
{id: 112, title: "Estudio NK (Mafanfa work)", category: "Agency & Studio",
 description: "3D digital branding company, featuring the Mafanfa project.", url: "https://estudionk.com/work/mafanfa"},
{id: 113, title: "Buck", category: "Agency & Studio",
 description: "Full-service creative agency, featuring their Pride Zine work.", url: "https://buck.co/work/pride-zine"},
{id: 114, title: "We are anagram", category: "Agency & Studio", description: "Experience design studio.",
 url: "https://weareanagram.co.uk/about"},
{id: 115, title: "Schultz & Schultz", category: "Agency & Studio",
 description: "German contemporary graphic design studio.", url: "https://www.schultzschultz.com/work.html"},
{id: 116, title: "Nguyen gobber", category: "Agency & Studio",
 description: "Design studio for academia, culture, and the social field.", url: "https://nguyengobber.com"},
{id: 117, title: "Locomotive", category: "Agency & Studio", description: "Motion design studio.",
 url: "https://locomotive.ca/en"},
{id: 118, title: "Peter Tarka", category: "Agency & Studio", description: "3D design agency led by Dan Foster.",
 url: "https://petertarka.com"},
{id: 119, title: "Arts cabinet publication", category: "Agency & Studio",
 description: "Online editorial and publication, linking to the Migration digital edition.",
 url: "https://www.artscabinet.org/publications/migration-01-digital-edition"},
{id: 120, title: "P-R studio", category: "Agency & Studio",
 description: "Branding, interiors, and live experience work.", url: "https://p-r.studio"},
{id: 121, title: "How studio", category: "Agency & Studio", description: "Branding agency portfolio.",
 url: "https://how.studio"},
{id: 122, title: "Oh mana", category: "Agency & Studio", description: "Amazing print and digital branding agency.",
 url: "http://oh-mana.com/index.html"},
{id: 123, title: "Untitled Macao", category: "Agency & Studio",
 description: "Contemporary branding, exhibition design, and original mockups (Chinese focus).",
 url: "https://untitledmacao.com/works"},
{id: 124, title: "Found studio", category: "Agency & Studio", description: "3D design agency.",
 url: "https://www.found-studio.com"},
{id: 125, title: "More and more ltd", category: "Agency & Studio", description: "3D branding studio.",
 url: "https://moreandmoreltd.com"},
{id: 126, title: "Nendo", category: "Agency & Studio", description: "3D branding and innovative design studio.",
 url: "https://www.nendo.jp"},
{id: 127, title: "Gretel NY", category: "Agency & Studio", description: "Mainstream New York based branding company.",
 url: "https://gretelny.com"},
{id: 128, title: "Lennarts & Debruijn", category: "Agency & Studio",
 description: "Fun, experimental graphic design company.", url: "https://lennartsendebruijn.com"},
{id: 129, title: "Oimachi", category: "Agency & Studio", description: "Digital branding agency.",
 url: "https://www.oimachi"},
{id: 130, title: "Brand new school", category: "Agency & Studio",
 description: "Digital branding with great case studies.", url: "https://www.brandnewschool.com"},
{id: 131, title: "Saffron consultants", category: "Agency & Studio", description: "Contemporary branding consultancy.",
 url: "https://saffron-consultants.com"},
{id: 132, title: "Project archive (Freytag Anderson)", category: "Agency & Studio",
 description: "Scottish branding agency, excellent photography and art direction.",
 url: "https://www.projectarchive.freytaganderson.com"},
{id: 133, title: "Studio size", category: "Agency & Studio", description: "Contemporary digital branding agency.",
 url: "https://studio-size.com"},
{id: 134, title: "Commission studio", category: "Agency & Studio",
 description: "Great art direction and product branding focus.", url: "https://www.commission.studio"},
{id: 1103, title: "Boldly foods", category: "Agency & Studio",
 description: "Plant-based food brand with exceptional web design and branding.", url: "https://www.boldlyfoods.com"},
{id: 1120, title: "Pentagram", category: "Agency & Studio",
 description: "The world’s largest independently-owned design studio.", url: "https://www.pentagram.com/"},

// --- Typography - --
{id: 201, title: "Typetype fonts", category: "Typography",
 description: "Good variation in trial fonts for testing and exploration.", url: "https://typetype.org/fonts"},
{id: 202, title: "Rosetta type foundry", category: "Typography",
 description: "An excellent source for free variable fonts.", url: "https://rosettatype.com"},
{id: 203, title: "ABC Dinamo", category: "Typography",
 description: "Amazing type foundry with a mix of free and premium, high-quality typefaces.",
 url: "https://abcdinamo.com"},
{id: 204, title: "Type foundry directory", category: "Typography",
 description: "A comprehensive directory listing various type foundries.", url: "https://typefoundry.directory"},
{id: 205, title: "Oh no type co", category: "Typography",
 description: "Funky, unique, and loud experimental typefaces.", url: "https://ohnotype.co"},
{id: 206, title: "Typothèque", category: "Typography",
 description: "Foundry offering display, corporate, and elegantly reductive fonts.",
 url: "https://www.typothxeque.com"},
{id: 207, title: "Fonts in use", category: "Theory",
 description: "Resource for font research and examples of typography used in real-world contexts.",
 url: "https://fontsinuse.com"},
{id: 208, title: "Colophon foundry", category: "Typography",
 description: "Independent type foundry focusing on custom and retail typefaces.",
 url: "https://www.colophon-foundry.org"},
{id: 209, title: "Art of the title (1980s)", category: "Publications & Archives",
 description: "Archive of title sequences, focused on 1980s typography and design styles.",
 url: "https://www.artofthetitle.com/style/1980s"},
{id: 210, title: "Velvetyne", category: "Typography", description: "Free and experimental open-source type foundry.",
 url: "https://velvetyne.fr/fonts"},
{id: 211, title: "Awwwards free fonts", category: "Typography",
 description: "Curated collection of free, contemporary fonts.",
 url: "https://www.awwwards.com/awwwards/collections/free-fonts"},
{id: 212, title: "Optimo", category: "Typography", description: "Independent type foundry based in Geneva.",
 url: "https://optimo.ch"},
{id: 213, title: "Klim type foundry", category: "Typography",
 description: "High-quality type foundry, known for amazing 3D typography examples.", url: "https://klim.co.nz"},
{id: 214, title: "Logo design love", category: "Logos",
 description: "Resource for logo design, branding, and identity.", url: "https://www.logodesignlove.com"},
{id: 215, title: "Collletttivo", category: "Typography", description: "Open source type foundry.",
 url: "http://www.collletttivo.it"},
{id: 216, title: "Lineto", category: "Typography",
 description: "Experimental type foundry with unique and challenging typefaces.", url: "https://lineto.com"},
{id: 217, title: "Le signe", category: "Publications & Archives",
 description: "National Graphic Design Exhibition center in France.",
 url: "http://www.centrenationaldugraphisme.fr/en/le-signe/presentation"},
{id: 218, title: "Atipo foundry", category: "Typography", description: "Contemporary type foundry.",
 url: "https://www.atipofoundry.com"},
{id: 219, title: "Fontshare", category: "Typography", description: "Cool collection of free, high-quality fonts.",
 url: "https://www.fontshare.com"},
{id: 220, title: "Pangram pangram", category: "Typography",
 description: "Contemporary type foundry with test fonts available.", url: "https://pangrampangram.com"},
{id: 221, title: "MA-MA type (Monospace)", category: "Typography",
 description: "Type foundry that sells the Brook Monospace typeface.", url: "https://ma-ma-type.com"},
{id: 222, title: "In the shade of a tree", category: "Publications & Archives",
 description: "London / Paris based print design company.", url: "http://in-the-shade-of-a-tree.com"},
{id: 223, title: "BNicks shop", category: "Typography", description: "Source for cheap and fun typefaces.",
 url: "https://www.bnicks.com/shop"},
{id: 224, title: "Divina lingua", category: "Typography",
 description: "Digital poetry project focused on Dante's typography.", url: "https://divinalingua.it/en"},
{id: 225, title: "Vintage business cards (Flickr)", category: "Publications & Archives",
 description: "Flickr group archive of vintage business cards.",
 url: "https://www.flickr.com/groups/vintage_business_cards/pool/page2"},
{id: 226, title: "Logo book", category: "Logos", description: "Digital archive of logo designs.",
 url: "http://www.logobook.com"},
{id: 227, title: "Logo core (Pinterest)", category: "Logos",
 description: "Pinterest archive collection of logo designs.", url: "https://www.pinterest.ca/logocore/logo-archive"},
{id: 228, title: "NAN typefaces", category: "Typography",
 description: "Contemporary trial typefaces available for testing.", url: "https://www.nan.xyz/fonts"},
{id: 229, title: "The inspiration grid", category: "Publications & Archives",
 description: "Generic design inspiration website.", url: "https://theinspirationgrid.com"},
{id: 230, title: "Estudio CRU", category: "Agency & Studio",
 description: "Brazilian design studio focused on branding.", url: "https://www.estudiocru.com/en"},
{id: 231, title: "Tiago baptista", category: "Designer Portfolio",
 description: "Portfolio featuring a beautiful website layout.", url: "https://www.tiagobaptista.pt/index.html"},
{id: 232, title: "Blaze type", category: "Typography", description: "Contemporary type foundry.",
 url: "https://blazetype.eu"},
{id: 233, title: "Behance dancing lettering", category: "Designer Portfolio",
 description: "Textured animation example on Behance.", url: "https://www.behance.net/gallery/153761521/DANCING"},
{id: 234, title: "CRSL studio (Switch work)", category: "Agency & Studio",
 description: "Amazing website design case study by CRSL Studio.", url: "https://crsl.studio/works/switch"},
{id: 235, title: "MM Paris typographic book", category: "Publications & Archives",
 description: "Design week article on a typographic book by MM Paris.", url: "https://www.designweek.co.uk"},
{id: 236, title: "Dalton Maag (Greta)", category: "Typography",
 description: "Mainstream type foundry offering the Greta typeface for testing.", url: "https://www.daltonmaag.com"},
{id: 237, title: "F37 foundry", category: "Typography", description: "Contemporary foundry offering free test fonts.",
 url: "https://f37foundry.com"},
{id: 238, title: "Zetafonts", category: "Typography", description: "Italian fun type foundry offering free fonts.",
 url: "https://www.zetafonts.com"},
{id: 239, title: "Letterform archive", category: "Publications & Archives",
 description: "Online archive of graphic design and typography history (OA section).",
 url: "https://oa.letterformarchive.org"},
{id: 240, title: "Branding style guides", category: "Theory", description: "Collection of public brand guidelines.",
 url: "https://brandingstyleguides.com"},
{id: 241, title: "Sawdust", category: "Agency & Studio", description: "Amazing 3D design studio.",
 url: "https://sawdust.works"},
{id: 242, title: "MVSM", category: "Agency & Studio", description: "3D advertising agency.", url: "https://mvsm.com"},
{id: 243, title: "Mucho", category: "Agency & Studio",
 description: "Interesting, simple design agency, similar style to Pentagram.", url: "https://wearemucho.com/work"},
{id: 244, title: "Bulgarian logo archive (ABVA)", category: "Logos", description: "Bulgarian logo archive.",
 url: "https://archive.abva.bg/en/items?q=logo"},
{id: 245, title: "Proxy VC", category: "Agency & Studio",
 description: "Forward-thinking design for good tech companies.", url: "https://proxy.vc"},
{id: 246, title: "Nocliches", category: "Publications & Archives", description: "Design archive and inspiration site.",
 url: "https://noclich.es"},
{id: 247, title: "Oker", category: "Agency & Studio", description: "High-quality 3D branding agency.",
 url: "https://oker.com"},
{id: 248, title: "Buy fonts save lives", category: "Typography", description: "Type foundry with a social mission.",
 url: "https://buyfontssavelives.com/fonts"},
{id: 249, title: "Site inspire", category: "Publications & Archives",
 description: "Design website bank, similar to Awwwards.", url: "https://www.siteinspire.com"},
{id: 250, title: "Micaela brazerol", category: "Designer Portfolio",
 description: "Portfolio of a cool poster designer.", url: "https://micaelabrazerol.ch/index.php"},
{id: 251, title: "Atelier lomann", category: "Agency & Studio", description: "German design company.",
 url: "https://atelier-lomann.ch"},
{id: 252, title: "Lomann lab", category: "Publications & Archives",
 description: "Section of Atelier Lomann with cool objects and images.",
 url: "https://lab.atelier-lomann.ch/lomann-lab"},
{id: 253, title: "Typemates", category: "Typography", description: "Commercial type foundry.",
 url: "https://www.typemates.com"},
{id: 254, title: "Bblamage fonts", category: "Typography", description: "Experimental type foundry.",
 url: "http://www.bblamage-fonts.net"},
{id: 255, title: "ECAL typefaces", category: "Typography", description: "Archive of experimental typefaces from ECAL.",
 url: "https://ecal-typefaces.ch/typeface"},
{id: 256, title: "Typeroom", category: "Publications & Archives", description: "Online type magazine.",
 url: "https://www.typeroom.eu"},
{id: 257, title: "Fontbrief", category: "Tools",
 description: "Font resource with good categories filters for typefaces.", url: "https://www.fontbrief.com/fontbrief"},
{id: 258, title: "Cartlidge levene", category: "Agency & Studio",
 description: "Great resource for print design and grid systems.", url: "https://cartlidgelevene.co.uk"},
{id: 259, title: "Wordmark.it", category: "Tools", description: "Tool for testing word marks with local fonts.",
 url: "https://wordmark.it"},
{id: 260, title: "Miratrix brutalist font", category: "Typography",
 description: "A free brutalist font inspiration link from Awwwards.",
 url: "https://www.awwwards.com/inspiration/miratrix-brutalist-font"},
{id: 261, title: "Open foundry", category: "Typography", description: "Open source type foundry.",
 url: "https://open-foundry.com/fonts"},
{id: 262, title: "Are.na open source typefaces", category: "Publications & Archives",
 description: "Artistic and original open-source typeface collection on Are.na.",
 url: "https://www.are.na/frederic-brodbeck/open-source-typefaces"},
{id: 263, title: "Merchery co", category: "Mockups & Assets",
 description: "Source for premium swag and mockup templates.", url: "https://merchery.co"},
{id: 264, title: "Arillatype studio", category: "Typography",
 description: "Amazing branding type foundry with type trials and cheap licensing.", url: "https://arillatype.studio"},
{id: 265, title: "Kurppa Hosk", category: "Agency & Studio", description: "Stockholm branding agency and type foundry.",
 url: "https://www.kurppahosk.com/work"},
{id: 1108, title: "Studio Feixen fonts", category: "Typography",
 description: "The type foundry of the Swiss design studio Feixen.", url: "https://fonts.studiofeixen.ch"},

// --- Mockups & Assets - --
{id: 301, title: "Rico supply", category: "Mockups & Assets", description: "Motion template and asset resource.",
 url: "https://rico.supply/categories/all"},
{id: 302, title: "Orbyt studio", category: "Mockups & Assets",
 description: "Source for sexy B2B mockups. (URL not provided)", url: "#"},
{id: 303, title: "Mockup maison", category: "Mockups & Assets",
 description: "City-based mockup templates. (URL not provided)", url: "#"},
{id: 304, title: "Texture labs", category: "Mockups & Assets", description: "Digital texture resources.",
 url: "https://texturelabs.org"},
{id: 305, title: "Texture fabrik", category: "Mockups & Assets", description: "Fabric texture resources.",
 url: "https://texturefabrik.com/tag/texture-fabric"},
{id: 306, title: "Studio 2AM", category: "Mockups & Assets",
 description: "Resource to buy texture assets, good for Photoshop.", url: "https://www.studio2am.co"},
{id: 307, title: "Fix the photo overlays", category: "Mockups & Assets",
 description: "Vintage Photoshop overlay resources.", url: "https://fixthephoto.com/vintage-overlay"},
{id: 1104, title: "Pitch templates", category: "Mockups & Assets",
 description: "Presentation templates and design inspiration for decks.", url: "https://pitch.com/templates"},

// --- Publications & Archives - --
{id: 401, title: "Logo archive magazine shop", category: "Publications & Archives",
 description: "Online shop for Logo Archive magazine.", url: "https://www.logoarchive.shop"},
{id: 402, title: "TM research archive", category: "Publications & Archives",
 description: "Archive of magazine covers and publication design research.", url: "http://www.tm-research-archive.ch"},
{id: 403, title: "Type-01 magazine", category: "Publications & Archives",
 description: "Contemporary type magazine (yearly subscription suggestion).", url: "https://type-01.com/checkout"},
{id: 404, title: "Man and his mark (Logo print)", category: "Logos",
 description: "Logo print book resource from Logo Design Love.",
 url: "https://www.logodesignlove.com/man-and-his-mark"},
{id: 1102, title: "Made in Webflow", category: "Publications & Archives",
 description: "A showcase of websites built with Webflow.", url: "https://webflow.com/made-in-webflow/likes"},
{id: 1109, title: "Awwwards", category: "Publications & Archives",
 description: "The awards for design, creativity and innovation on the Internet.", url: "https://www.awwwards.com"},

// --- Reading
List - --
{id: 501, title: "Typewolf typography books", category: "Reading List",
 description: "A curated list of essential typography books from Typewolf.",
 url: "https://www.typewolf.com/typography-books"},

// --- Material & Print - --
{id: 601, title: "Arjowiggins alchemy paper", category: "Material & Print",
 description: "Bespoke Curious Collection Alchemy paper in Gold Au.",
 url: "https://www.arjowigginscreativepapers.com/en/catalog/curious-collection/alchemy/gold-au"},
{id: 602, title: "Arjowiggins", category: "Material & Print", description: "Local paper company resources.",
 url: "https://www.arjowiggins.com"},

// --- Designer
Portfolio - --
{id: 701, title: "Miniature calendar", category: "Designer Portfolio",
 description: "Visual play and miniature home sets by Tanaka Tatsuya.", url: "https://miniature-calendar.com"},
{id: 702, title: "Cake porn time", category: "Designer Portfolio",
 description: "Portfolio of a cake artist and Japanese product design.", url: "https://www.cakeporntime.com"},
{id: 703, title: "Anita fontaine", category: "Designer Portfolio",
 description: "AR & Print designer, featuring 'New Realities' and Moncler work.",
 url: "https://anitafontaine.com/new-realities"},
{id: 704, title: "Cliff studio", category: "Designer Portfolio", description: "Portfolio of web designer Cliff.",
 url: "http://www.cliff.studio"},
{id: 705, title: "Ezekiel aquino", category: "Designer Portfolio",
 description: "Experimental generated code and design portfolio, featuring 'Panels'.",
 url: "https://ezekielaquino.com/2019/panels"},
{id: 706, title: "Charlie le maignan", category: "Designer Portfolio",
 description: "Portfolio specializing in kinetic type design.", url: "https://charlielemaignan.com"},
{id: 707, title: "Connor campbell", category: "Designer Portfolio",
 description: "Portfolio specializing in kinetic type design.", url: "http://connorcampbell.studio"},
{id: 708, title: "Thomas burden", category: "Designer Portfolio", description: "Illustrator from Handsome Frank.",
 url: "https://www.handsomefrank.com/illustrators/thomas-burden"},
{id: 709, title: "Fons hickmann", category: "Designer Portfolio", description: "German experimental design portfolio.",
 url: "https://fonshickmann.com/work"},
{id: 710, title: "Mario ECG", category: "Designer Portfolio", description: "Creative coder portfolio.",
 url: "https://marioecg.com"},

// --- Sound & Audio - --
{id: 801, title: "Burning witches records", category: "Sound & Audio", description: "Music and record label releases.",
 url: "https://burningwitchesrecords.com/releases/ncchm2vel06hookfghod4rlzy0dj71"},
{id: 802, title: "Sounds like these", category: "Sound & Audio",
 description: "Sound design and music resource, featuring the 'Beat Club / Banana' project.",
 url: "https://soundslikethese.com/beat-club/banana"},

// --- Tools - --
{id: 901, title: "Color hunt", category: "Tools", description: "Curated color palettes for design inspiration.",
 url: "https://colorhunt.co"},
{id: 902, title: "Coolors trending palettes", category: "Tools",
 description: "Trending color palettes and generator tool.", url: "https://coolors.co/palettes/trending"},
{id: 903, title: "Pigment", category: "Tools", description: "Interactive color palette generator from Shape Factory.",
 url: "https://pigment.shapefactory.co"},
{id: 1110, title: "Mobbin", category: "Tools",
 description: "Comprehensive library of mobile and web app design patterns.",
 url: "https://mobbin.com/discover/sites/latest"},
{id: 1101, title: "GSAP showcase", category: "Tools",
 description: "Showcase of websites using the GreenSock Animation Platform for high-performance animations.",
 url: "https://gsap.com/showcase"},

// --- Iconography - --
{id: 1105, title: "Hugeicons", category: "Iconography",
 description: "High-quality icon library for designers and developers.", url: "https://hugeicons.com"},
{id: 1106, title: "Lucide icons", category: "Iconography",
 description: "Beautiful & consistent icon toolkit for the modern web.", url: "https://lucide.dev/icons"},
{id: 1107, title: "Heroicons", category: "Iconography",
 description: "Beautiful hand-crafted SVG icons, by the makers of Tailwind CSS.", url: "https://heroicons.com"},

// --- Architecture - --
{id: 1001, title: "OMA", category: "Architecture",
 description: "Office for Metropolitan Architecture (OMA) firm portfolio.", url: "https://www.oma.com"},
{id: 1002, title: "2m26", category: "Architecture", description: "Wood architects based in Tokyo, Japan.",
 url: "https://2m26.com"},
{id: 1003, title: "Bard architecture", category: "Architecture", description: "Architecture community resource.",
 url: "https://arch.bard.edu"},
];

// Component
for adding a new reference
const AddReferenceForm = ({allCategories, onAdd, onClose, isDarkMode}) = > {
const
filterableCategories = allCategories.filter(c= > c != = 'All' & & c != = 'Discover');
const[formData, setFormData] = useState({
    title: '',
    category: filterableCategories[0] | | 'Typography',
    description: '',
    url: 'https://',
});

const
handleChange = (e) = > {
    const
{name, value} = e.target;
setFormData(prev= > ({...prev, [name]: value}));
};

const
handleSubmit = (e) = > {
    e.preventDefault();
if (formData.title & & formData.description & & formData.url)
{
    onAdd({
        ...
formData,
id: Date.now(),
category: formData.category | | 'Miscellaneous'
});
onClose();
}
};

const
formBg = isDarkMode ? 'bg-[#111] text-white': 'bg-[#fcfbf8] text-neutral-800';
const
inputBg = isDarkMode ? 'bg-[#222] border-gray-700 text-white': 'bg-white border-gray-300 text-neutral-800';
const
buttonBg = isDarkMode ? 'bg-white text-black hover:bg-gray-200': 'bg-neutral-800 text-[#f9f7f4] hover:bg-indigo-600';

return (
    < div className="fixed inset-0 bg-neutral-900/80 flex items-center justify-center z-50 p-4 font-sans" >
    < div className={`${formBg} p-6 sm:p-8 w-full max-w-lg shadow-2xl`} >
    < div className={`flex justify-between items-center border-b ${isDarkMode ? 'border-gray-700': 'border-gray-300/50'} pb-4 mb-6`} >
    < h2 className="text-xl font-semibold" > Add New Reference < / h2 >
    < button onClick={onClose} className={isDarkMode ? 'text-gray-400 hover:text-white': 'text-gray-500 hover:text-neutral-800'} >
    < X className="w-5 h-5" / >
    < / button >
    < / div >

    < form onSubmit={handleSubmit} className="space-y-4" >
    < div >
    < label className={`block text-sm font-medium ${isDarkMode ? 'text-gray-300': 'text-neutral-700'}`} > Title < / label >
    < input
    type="text"
    name="title"
    value={formData.title}
    onChange={handleChange}
    required
    className={`mt-1 block w-full p-2 focus:outline-none focus:border-indigo-500 ${inputBg}`}
    / >
    < / div >
    < div >
    < label className={`block text-sm font-medium ${isDarkMode ? 'text-gray-300': 'text-neutral-700'}`} > Category < / label >
    < select
    name="category"
    value={formData.category}
    onChange={handleChange}
    required
    className={`mt-1 block w-full p-2 focus:outline-none focus:border-indigo-500 ${inputBg}`}
    >
    {filterableCategories.map(cat = > (
    < option key={cat} value={cat} > {cat} < / option >
))}
< / select >
    < / div >
        < div >
        < label
className = {`block
text - sm
font - medium ${isDarkMode ? 'text-gray-300': 'text-neutral-700'}`} > Description < / label >
                                                                                      < textarea
name = "description"
value = {formData.description}
onChange = {handleChange}
required
rows = "3"
className = {`mt - 1
block
w - full
p - 2
focus: outline - none
focus: border - indigo - 500 ${inputBg}
`}
> < / textarea >
      < / div >
          < div >
          < label
className = {`block
text - sm
font - medium ${isDarkMode ? 'text-gray-300': 'text-neutral-700'}`} > URL < / label >
                                                                              < input
type = "url"
name = "url"
value = {formData.url}
onChange = {handleChange}
required
className = {`mt - 1
block
w - full
p - 2
focus: outline - none
focus: border - indigo - 500 ${inputBg}
`}
/ >
< / div >
    < button
type = "submit"
className = {`w - full
py - 2
font - medium
transition
duration - 150 ${buttonBg}
`}
>
Add
Reference
< / button >
    < / form >
        < / div >
            < / div >
);
};

// 1.
List
View
Component
const
ReferenceListCard = ({reference, isDarkMode}) = > (
< a
href = {reference.url}
target = "_blank"
rel = "noopener noreferrer"
className = {`block
py - 12
first: pt - 0
border - b ${isDarkMode ? 'border-neutral-800 hover:bg-white/5': 'border-gray-300/50 hover:bg-neutral-100'} transition
duration - 150
group
cursor - pointer
relative
z - 10
`}
>
< div
className = "flex flex-col" >
< div
className = "mb-4" >
< h3
className = {`text - xl
sm: text - 2
xl
font - light ${isDarkMode ? 'text-neutral-200': 'text-neutral-800'} leading - tight
`} >
{reference.title}
< / h3 >
< / div >
< div
className = "flex flex-col sm:flex-row sm:items-end justify-between text-sm" >
< div
className = "sm:w-3/4 sm:pr-8 mb-4 sm:mb-0" >
< p
className = {`${isDarkMode ? 'text-neutral-400': 'text-neutral-600'} leading - relaxed
`} > {reference.description} < / p >
< / div >
< div
className = "flex-shrink-0 self-start sm:self-end" >
< span
className = {`text - [11px]
font - medium
border
px - 1.5
py - 0.5
whitespace - nowrap ${getCategoryColors(reference.category, isDarkMode)}
`} >
{reference.category}
< / span >
< / div >
< / div >
< / div >
< / a >
);

// 2.
Grid
View
Component
const
ReferenceGridCard = ({reference, isDarkMode}) = > (
< a
href = {reference.url}
target = "_blank"
rel = "noopener noreferrer"
className = {`block
bg - transparent
p - 4
md: p - 5
border ${isDarkMode ? 'border-neutral-800 hover:border-gray-500': 'border-gray-300/50 hover:border-gray-500'} transition
duration - 300
flex
flex - col
h - full
group
cursor - pointer
relative
z - 10
`}
>
< div
className = "flex justify-between items-start mb-1" >
< span
className = {`text - [10px]
font - medium
border
px - 1.5
py - 0.5
whitespace - nowrap ${getCategoryColors(reference.category, isDarkMode)}
`} >
{reference.category}
< / span >
< Link
className = {`w - 3
h - 3 ${
    isDarkMode ? 'text-gray-600 group-hover:text-neutral-300': 'text-gray-400 group-hover:text-neutral-800'} transition - colors
mt - 1
`} / >
< / div >

< div
className = "mt-3 flex-grow" >
< h3
className = {`text - xl
font - medium ${
    isDarkMode ? 'text-neutral-200 group-hover:text-neutral-400': 'text-neutral-800 group-hover:text-neutral-600'} leading - snug
mb - 3
transition - colors
`} >
{reference.title}
< / h3 >

< p
className = {`text - sm ${isDarkMode ? 'text-neutral-500': 'text-neutral-600'} leading - tight
line - clamp - 4
`} >
{reference.description}
< / p >
< / div >
< / a >
);

// Main
Application
Component
function
App()
{
const[references, setReferences] = useState(INITIAL_USER_DATA);
const[searchQuery, setSearchQuery] = useState('');
const[activeCategory, setActiveCategory] = useState('All');
const[isAddingReference, setIsAddingReference] = useState(false);
const[viewMode, setViewMode] = useState('list');
const[isDarkMode, setIsDarkMode] = useState(false);

const
toggleTheme = () = > setIsDarkMode(!isDarkMode);

const
currentCategories = useMemo(() = > {
    const
categories = [...new Set(references.map(ref= > ref.category))].sort((a, b) = > a.localeCompare(b));
const
filteredCategories = categories.filter(c= > c != = 'All');
return ['All', 'Discover', ...filteredCategories];
}, [references]);

const
handleAddReference = (newRef) = > {
    setReferences(prevRefs= > [...prevRefs, newRef]);
};

const
filteredReferences = useMemo(() = > {
let
result = references;
if (searchQuery.trim() !== '') {
const lowerCaseQuery = searchQuery.toLowerCase();
result = result.filter(ref = >
ref.title.toLowerCase().includes(lowerCaseQuery) | |
ref.description.toLowerCase().includes(lowerCaseQuery)
);
}

if (activeCategory === 'Discover') {
return [...result].sort(() = > Math.random() - 0.5);
} else if (activeCategory !== 'All') {
result = result.filter(ref= > ref.category == = activeCategory);
}

return [...result].sort((a, b) = > a.title.localeCompare(b.title));
}, [references, activeCategory, searchQuery]);

const
appBg = isDarkMode ? 'bg-[#111]': 'bg-[#f9f7f4]';
const
textMain = isDarkMode ? 'text-neutral-200': 'text-neutral-800';
const
textSub = isDarkMode ? 'text-neutral-500': 'text-neutral-500';
const
borderBase = isDarkMode ? 'border-neutral-800': 'border-gray-300/50';
const
inputBg = isDarkMode ? 'bg-[#111] border-neutral-700 text-neutral-200': 'bg-[#f9f7f4] border-neutral-800 text-neutral-800';

return (
    < div className={`min-h-screen ${appBg} font-sans transition-colors duration-300`} >
    {isAddingReference & & (
    < AddReferenceForm
    allCategories={currentCategories}
    onAdd={handleAddReference}
    onClose={() = > setIsAddingReference(false)}
isDarkMode = {isDarkMode}
             / >
)}

< div
className = "max-w-6xl mx-auto px-6 sm:px-12 pt-12" >

            < h1
className = {`w - full
text - 4
xl
sm: text - 6
xl
md: text - 8
xl
font - light ${textMain}
mb - 8
tracking - tighter
uppercase
leading - none
break
-words
`} >
ALL
THINGS
ARE
DESIGNED
< / h1 >

    < div
className = {`sticky
top - 0
z - 40 ${appBg}
pt - 4
pb - 4
border - b - 0
transition - colors
duration - 300
`} >
< div
className = "flex flex-col gap-4" >
            < div
className = "flex flex-col sm:flex-row justify-between items-center gap-4" >
            < div
className = {`relative
w - full
sm: w - 2 / 3 ${inputBg}
border
rounded - none
`} >
< input
type = "text"
placeholder = "Search..."
value = {searchQuery}
onChange = {(e) = > setSearchQuery(e.target.value)}
className = {`w - full
pl - 10
pr - 4
py - 2
text - sm
placeholder - neutral - 500
bg - transparent
focus: outline - none
focus: ring - 0
focus: border - indigo - 500
transition
duration - 150
`}
/ >
< Search
className = "w-4 h-4 absolute left-3 top-1/2 transform -translate-y-1/2 text-neutral-500" / >
            < / div >

                < div
className = "flex items-center gap-4 w-full sm:w-1/3" >
            < button
onClick = {() = > setIsAddingReference(true)}
className = {`flex - grow
py - 2
text - sm
flex
items - center
justify - center
font - medium
transition
duration - 150
tracking - wide ${
    isDarkMode ? 'bg-white text-black hover:bg-gray-200': 'bg-neutral-800 text-[#f9f7f4] hover:bg-indigo-600'}`}
>
< Plus
className = "w-4 h-4 mr-2" / >
            Add
            < / button >

                < div
className = "flex items-center gap-2" >
            < button
onClick = {toggleTheme}
className = {`p - 2
rounded - sm
border ${
    isDarkMode ? 'border-gray-700 text-yellow-400 hover:text-yellow-300': 'border-gray-300 text-gray-400 hover:text-gray-900'} ${
    appBg}
`}
title = {isDarkMode ? "Switch to Light Mode": "Switch to Dark Mode"}
>
{isDarkMode ? < Sun
className = "w-4 h-4" / >: < Moon
className = "w-4 h-4" / >}
< / button >

    < div
className = {`flex ${appBg}
border ${isDarkMode ? 'border-gray-700': 'border-gray-300'} rounded - sm
overflow - hidden
`} >
< button
onClick = {() = > setViewMode('list')}
className = {`p - 2 ${viewMode == = 'list' ? (isDarkMode ? 'bg-gray-800 text-white': 'bg-gray-200 text-gray-900'): (
    isDarkMode ? 'text-gray-500 hover:text-gray-300': 'text-gray-400 hover:text-gray-600')} transition - colors
`}
title = "List View"
        >
        < LayoutList
className = "w-4 h-4" / >
            < / button >
                < div
className = {`w - px ${isDarkMode ? 'bg-gray-700': 'bg-gray-300'}`} > < / div >
                                                                          < button
onClick = {() = > setViewMode('grid')}
className = {`p - 2 ${viewMode == = 'grid' ? (isDarkMode ? 'bg-gray-800 text-white': 'bg-gray-200 text-gray-900'): (
    isDarkMode ? 'text-gray-500 hover:text-gray-300': 'text-gray-400 hover:text-gray-600')} transition - colors
`}
title = "Grid View"
        >
        < LayoutGrid
className = "w-4 h-4" / >
            < / button >
                < / div >
                    < / div >
                        < / div >
                            < / div >

                                < div
className = "flex flex-wrap gap-2" >
            {currentCategories.map(category= > {
                const
isDiscover = category == = 'Discover';
return (
    < button
    key={category}
    onClick={() = > {
    setActiveCategory(category);
setSearchQuery('');
}}
className = {`
px - 2.5
py - 1
text - xs
font - medium
border
transition
duration - 200
tracking - wide
flex
items - center
${activeCategory == = category
? getActiveCategoryStyles(category, isDarkMode)
: `${getCategoryColors(category, isDarkMode)}
hover: bg - opacity - 10
hover: bg - gray - 500
`
}
`}
>
{isDiscover & & < Sparkles
className = "w-3 h-3 mr-1.5" / >}
{category}
< / button >
)
})}
< / div >
    < / div >
        < / div >

            < div
className = "pt-8" >
            {filteredReferences.length > 0 ? (
        viewMode === 'list' ? (
< div
className = "flex flex-col" >
{filteredReferences.map(ref= > (
    < ReferenceListCard key={ref.id} reference={ref} isDarkMode={isDarkMode} / >
))}
< / div >
): (
< div
className = "grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6" >
{filteredReferences.map(ref= > (
    < ReferenceGridCard key={ref.id} reference={ref} isDarkMode={isDarkMode} / >
))}
< / div >
)
): (
    < div className={`text-center py-20 border-b ${borderBase}`} >
    < p className={`text-xl ${textSub}`} >
    No references found for "{searchQuery}" in {activeCategory}.
    < / p >
    < / div >
)}
< / div >

    < div
className = "h-40" > < / div >
                         < / div >
                             < / div >
);
}

const
root = createRoot(document.getElementById('root'));
root.render( < App / >);
< / script >
    < / body >
        < / html >