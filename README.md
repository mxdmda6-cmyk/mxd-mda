# 🎉 16 Años: Interactive Day of the Dead Birthday Card 💀

An interactive web-based birthday card celebrating a special 16th birthday on Día de los Muertos (Day of the Dead). This digital card combines traditional Mexican cultural elements with modern web technology to create a unique, memorable experience.

## 🌟 Features

- **16 Interactive Memory Petals**: Click each marigold petal (numbered 1-16) to reveal memories from each year of life
- **Animated Sugar Skull**: Beautiful, interactive calavera (sugar skull) centerpiece with Day of the Dead decorations
- **Falling Marigold Petals**: Continuous animation of floating flower petals
- **Papel Picado Banners**: Traditional Mexican paper banner decorations that flutter at the top
- **Confetti Effects**: Celebratory confetti bursts when opening memories
- **Easter Eggs**: Hidden surprises including:
  - Multiple skull clicks reveal secret messages
  - Konami code activation (↑↑↓↓←→←→BA)
  - Special achievement for clicking all 16 petals
  - Triple and ultimate bonuses for persistence
- **Fully Responsive**: Works beautifully on desktop, tablet, and mobile devices
- **No Dependencies**: Pure HTML, CSS, and JavaScript - no frameworks required

## 🚀 Quick Start

### Option 1: Open Locally
1. Clone or download this repository
2. Open `index.html` in your web browser
3. Start clicking and exploring!

### Option 2: GitHub Pages (Recommended for Sharing)
1. Push this code to your GitHub repository
2. Go to Settings → Pages
3. Select the branch (usually `main`) and root folder
4. Your card will be live at: `https://yourusername.github.io/your-repo-name/`

### Option 3: Share via QR Code
1. Deploy to GitHub Pages or any web host
2. Generate a QR code for the URL using [qr-code-generator.com](https://www.qr-code-generator.com/)
3. Print the QR code on a physical card - scan to view the interactive experience!

## 📁 Project Structure

- **index.html** — Main birthday card HTML with structure
- **styles.css** — All styling, animations, and Day of the Dead theme
- **script.js** — Interactive functionality and easter eggs
- **docs/CANVA_GUIDE.md** — Guide for creating custom graphics with Canva

## 🎨 Customization Guide

### Personalizing Memories
Edit the `memories` object in `script.js` (starting at line 4) to customize each year's message:

```javascript
const memories = {
    1: {
        title: "Year 1 - Custom Title 🎈",
        content: "Your personalized memory for year 1..."
    },
    // ... customize all 16 years
};
```

### Adding Photos
You can add photos to memories by modifying the modal body in `script.js`:

```javascript
body.innerHTML = `
    <img src="path/to/photo.jpg" style="max-width: 100%; border-radius: 10px; margin-bottom: 15px;">
    <p>${memory.content}</p>
`;
```

### Changing Colors
Edit CSS variables in `styles.css` (lines 3-10) to customize the color scheme:

```css
:root {
    --marigold: #FFA500;
    --purple: #9D4EDD;
    --pink: #FF006E;
    /* ... more colors */
}
```

### Adding Music
Replace the audio element in `index.html` with a real audio file:

```html
<audio id="birthdayMusic" autoplay loop>
    <source src="las-mananitas.mp3" type="audio/mpeg">
</audio>
```

## 🎭 Cultural Significance

**Día de los Muertos (Day of the Dead)** is a Mexican holiday celebrated on November 1-2 that honors deceased loved ones. Key elements incorporated in this card:

- **Calaveras (Sugar Skulls)**: Decorated skulls representing departed souls
- **Marigolds (Cempasúchil)**: Flowers that guide spirits with their vibrant color and scent
- **Papel Picado**: Decorative paper banners with intricate cut designs
- **Vibrant Colors**: Celebration of life through bold, joyful colors

This card celebrates both a birthday and the beautiful tradition of honoring life and memory.

## 🎮 Easter Eggs & Secrets

Try to discover all the hidden features:
1. Click the sugar skull multiple times (especially 3 and 16 times!)
2. Use the Konami code on your keyboard: ↑↑↓↓←→←→BA
3. Click all 16 petals to unlock a special achievement
4. Check the browser console for hints (press F12)

## 🚀 Deployment Options

### GitHub Pages (Free)
- Push to GitHub
- Enable Pages in repository settings
- Share the URL

### Netlify (Free)
1. Drag and drop the folder to [netlify.com/drop](https://netlify.com/drop)
2. Get an instant shareable link

### Vercel (Free)
1. Install Vercel CLI: `npm i -g vercel`
2. Run `vercel` in project directory
3. Follow prompts for instant deployment

## 🎯 Future Ideas

- Add voice recording messages for each year
- Include photo gallery integration
- Add Instagram/social media sharing
- Create year-specific video clips
- Build a family collaboration feature (pull requests for memories!)
- Add multiple language support
- Create a "time capsule" feature for future birthdays

## 🤝 Contributing

This is a personal project, but feel free to fork and adapt it for your own celebrations! If you create something cool, share it back.

## 📝 License
Licensed under MIT (see **LICENSE**).

## 💖 Credits

Created with love for a special 16th birthday. Born on Día de los Muertos, forever celebrated with joy and color.

**¡Que viva la vida! 🎉💀🌺**
