import React, { useState } from 'react';

// Example distribution items. Adjust as needed.
const initialDistribution = [
  { label: 'Card Advantage', value: 8 },
  { label: 'Ramp', value: 7 },
  { label: 'Disruption', value: 6 },
  { label: 'Land', value: 37 },
  { label: 'Creature', value: 20 },
  { label: 'Artifact', value: 5 },
  { label: 'Enchantment', value: 5 },
  { label: 'Planeswalker', value: 1 },
  { label: 'Sorcery', value: 5 },
  { label: 'Instant', value: 5 },
];

const App = () => {
  const [commander, setCommander] = useState('');
  const [theme, setTheme] = useState('');
  const [distribution, setDistribution] = useState(initialDistribution);

  // Calculate total
  const totalCards = distribution.reduce((acc, item) => acc + item.value, 0);

  // Prevent total > 99
  const handleSliderChange = (index, newValue) => {
    const newVal = parseInt(newValue, 10);
    if (isNaN(newVal)) return;

    const sumExceptCurrent = distribution.reduce((acc, item, i) =>
      i === index ? acc : acc + item.value, 0
    );
    const newSum = sumExceptCurrent + newVal;

    if (newSum > 99) {
      alert('The total number of cards cannot exceed 99.');
      return;
    }

    setDistribution((prev) =>
      prev.map((item, i) =>
        i === index ? { ...item, value: newVal } : item
      )
    );
  };

  // POST the data to FastAPI (http://localhost:8000/save-deck)
  const handleGenerateDeck = async () => {
    const deckData = {
      commander,
      theme,
      distribution,
    };

    try {
      const response = await fetch("http://localhost:8000/save-deck", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(deckData),
      });

      if (!response.ok) {
        throw new Error("Failed to save deck");
      }

      const result = await response.json();
      console.log("Deck saved successfully:", result);
      alert("Deck saved successfully!");
    } catch (error) {
      console.error("Error saving deck:", error);
      alert("Error saving deck. Check console for details.");
    }
  };

  return (
    <div style={styles.appContainer}>
      <h1 style={styles.title}>Test Deck Builder</h1>
      <p style={styles.subtitle}>Build a commander deck with specific card type ratios</p>

      {/* Commander */}
      <div style={styles.section}>
        <label htmlFor="commander" style={styles.label}>Commander</label>
        <input
          id="commander"
          placeholder="Search for cards..."
          style={styles.input}
          value={commander}
          onChange={(e) => setCommander(e.target.value)}
        />
        <p style={styles.helperText}>Search for Magic cards to add to your deck</p>
      </div>

      {/* Theme */}
      <div style={styles.section}>
        <label htmlFor="theme" style={styles.label}>Theme (Optional)</label>
        <input
          id="theme"
          placeholder="e.g. Dragons, Lifegain, Tokens"
          style={styles.input}
          value={theme}
          onChange={(e) => setTheme(e.target.value)}
        />
      </div>

      {/* Distribution Sliders */}
      <div style={styles.distributionContainer}>
        <h2 style={styles.sectionHeader}>Card Type Distribution</h2>
        {distribution.map((item, index) => (
          <div style={styles.distRow} key={item.label}>
            <span style={styles.distCount}>{item.value} cards</span>
            <input
              type="range"
              min="0"
              max="60"
              value={item.value}
              onChange={(e) => handleSliderChange(index, e.target.value)}
              style={styles.slider}
            />
            <span style={styles.distLabel}>{item.label}</span>
          </div>
        ))}
      </div>

      {/* Total */}
      <div style={styles.totalContainer}>
        <h3 style={styles.totalText}>Total: {totalCards} cards</h3>
      </div>

      {/* Generate Deck Button */}
      <button style={styles.generateButton} onClick={handleGenerateDeck}>
        Generate Deck
      </button>
    </div>
  );
};

const styles = {
  appContainer: {
    minHeight: '100vh',
    margin: 0,
    padding: '1rem',
    color: '#fff',
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    backgroundColor: '#3c0f4f',
  },
  title: {
    marginTop: '1rem',
    fontSize: '1.8rem',
  },
  subtitle: {
    marginTop: '0.5rem',
    marginBottom: '2rem',
    fontSize: '0.95rem',
    color: '#d1b3e0',
  },
  section: {
    marginBottom: '1.5rem',
    width: '90%',
    maxWidth: '400px',
    display: 'flex',
    flexDirection: 'column',
  },
  label: {
    marginBottom: '0.4rem',
    fontSize: '1rem',
    fontWeight: 'bold',
  },
  input: {
    padding: '0.6rem',
    borderRadius: '4px',
    border: '1px solid #ccc',
    fontSize: '1rem',
    outline: 'none',
    marginBottom: '0.4rem',
  },
  helperText: {
    fontSize: '0.8rem',
    color: '#d1b3e0',
  },
  distributionContainer: {
    width: '90%',
    maxWidth: '500px',
    backgroundColor: '#200b30',
    padding: '1.5rem',
    borderRadius: '6px',
    marginBottom: '1rem',
  },
  sectionHeader: {
    fontSize: '1.1rem',
    marginBottom: '1rem',
    borderBottom: '1px solid #b48eca',
    paddingBottom: '0.4rem',
  },
  distRow: {
    display: 'flex',
    alignItems: 'center',
    marginBottom: '0.7rem',
    gap: '0.5rem',
  },
  distCount: {
    minWidth: '80px',
    textAlign: 'right',
    fontWeight: 'bold',
    color: '#d1b3e0',
  },
  slider: {
    flex: 1,
    cursor: 'pointer',
  },
  distLabel: {
    minWidth: '80px',
    fontWeight: 'bold',
  },
  totalContainer: {
    marginBottom: '2rem',
  },
  totalText: {
    fontSize: '1.1rem',
    fontWeight: 'bold',
    color: '#fff',
  },
  generateButton: {
    backgroundColor: '#8358ff',
    color: '#fff',
    fontSize: '1rem',
    padding: '0.8rem 1.2rem',
    border: 'none',
    borderRadius: '4px',
    cursor: 'pointer',
    marginBottom: '2rem',
  },
};

export default App;

