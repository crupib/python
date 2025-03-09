import React, { useState, useEffect } from 'react';

const App = () => {
  const [commander, setCommander] = useState('');
  const [theme, setTheme] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('');
  const [countInput, setCountInput] = useState('1'); // Default count input
  const [categoryCounts, setCategoryCounts] = useState({});

  // Sorted list of categories with "Creatures" fixed.
  const options = [
    "Artifacts",
    "Card Draw",
    "Commander-Specific Tech",
    "Creatures",
    "Enchanments",
    "Instants",
    "Lands",
    "Ramp",
    "Removal",
    "Sorceries",
    "Synergistic Cards",
    "Win Conditions"
  ];

  // When the selected category changes, update the count input field
  // with the previously saved count (if any); otherwise, default to 1.
  useEffect(() => {
    if (selectedCategory) {
      const storedCount = categoryCounts[selectedCategory];
      setCountInput(storedCount !== undefined ? storedCount.toString() : '1');
    } else {
      setCountInput('1');
    }
  }, [selectedCategory, categoryCounts]);

  // Handle category selection from the dropdown.
  const handleCategoryChange = (e) => {
    setSelectedCategory(e.target.value);
  };

  // Save or update the count for the selected category.
  const saveCategoryCount = () => {
    if (!selectedCategory) return; // Do nothing if no category is selected
    const newCount = parseInt(countInput, 10);
    if (isNaN(newCount)) return; // Do nothing if the input is not a valid number

    setCategoryCounts((prevCounts) => ({
      ...prevCounts,
      [selectedCategory]: newCount
    }));
  };

  // Send the deck data to the FastAPI endpoint at http://localhost:8000/save-deck
  // The Python server will overwrite or create Deck.json on the server side.
  const handleSaveDeck = async () => {
    const deckData = {
      commander,
      theme: theme || "",
      categoryCounts,
    };

    try {
      const response = await fetch("http://localhost:8000/save-deck", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(deckData),
      });

      if (!response.ok) {
        throw new Error("Failed to save deck");
      }

      const result = await response.json();
      console.log("Deck saved successfully:", result);
      alert("Deck saved successfully!");

      // Clear the category data on success
      setCategoryCounts({});
      setSelectedCategory('');
      setCountInput('1');
    } catch (error) {
      console.error("Error saving deck:", error);
      alert("Error saving deck. Check console for details.");
    }
  };

  // Styling objects.
  const containerStyle = {
    backgroundColor: 'darkred',
    color: 'white',
    minHeight: '100vh',
    width: '100vw',
    display: 'flex',
    flexDirection: 'column',
  };

  const headerStyle = {
    textAlign: 'center',
    padding: '20px',
    fontSize: '24px',
  };

  const contentStyle = {
    flex: 1,
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'center', // Centers vertically
    alignItems: 'center',     // Centers horizontally
  };

  const rowStyle = {
    display: 'flex',
    alignItems: 'center',
    gap: '10px',
    marginBottom: '15px',
  };

  const labelStyle = {
    width: '150px',
    textAlign: 'right',
  };

  const inputStyle = {
    backgroundColor: 'yellow',
    border: '1px solid #ccc',
    padding: '5px',
    color: 'black',
    width: '200px',
  };

  const buttonStyle = {
    padding: '5px',
    backgroundColor: 'yellow',
    color: 'black',
    border: '1px solid #ccc',
    cursor: 'pointer',
  };

  return (
    <div style={containerStyle}>
      <header style={headerStyle}>
        Magic the Gathering Commander Deck Builder
      </header>

      <div style={contentStyle}>
        {/* Commander Row */}
        <div style={rowStyle}>
          <label htmlFor="commander" style={labelStyle}>
            Commander
          </label>
          <input
            type="text"
            id="commander"
            style={inputStyle}
            value={commander}
            onChange={(e) => setCommander(e.target.value)}
          />
        </div>

        {/* Theme Row */}
        <div style={rowStyle}>
          <label htmlFor="theme" style={labelStyle}>
            Theme
          </label>
          <input
            type="text"
            id="theme"
            style={inputStyle}
            value={theme}
            onChange={(e) => setTheme(e.target.value)}
          />
        </div>

        {/* Category Row */}
        <div style={rowStyle}>
          <label htmlFor="category" style={labelStyle}>
            Category
          </label>
          <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
            <select
              id="category"
              value={selectedCategory}
              onChange={handleCategoryChange}
              style={inputStyle}
            >
              <option value="">Select a Category</option>
              {options.map((option) => (
                <option key={option} value={option}>
                  {option}
                </option>
              ))}
            </select>

            <input
              type="number"
              value={countInput}
              onChange={(e) => setCountInput(e.target.value)}
              style={{ ...inputStyle, width: '80px' }}
            />

            <button onClick={saveCategoryCount} style={buttonStyle}>
              Keep
            </button>
          </div>
        </div>

        {/* Display saved category counts */}
        {Object.keys(categoryCounts).length > 0 && (
          <div style={{ ...rowStyle, justifyContent: 'center' }}>
            <ul style={{ listStyle: 'none', padding: 0, margin: 0 }}>
              {Object.entries(categoryCounts).map(([cat, count]) => (
                <li key={cat}>
                  {cat}: {count}
                </li>
              ))}
            </ul>
          </div>
        )}

        {/* Save Deck Button */}
        <div style={rowStyle}>
          {/* An empty label area to keep alignment */}
          <div style={{ width: '150px' }}></div>
          <button onClick={handleSaveDeck} style={buttonStyle}>
            Save Deck
          </button>
        </div>
      </div>
    </div>
  );
};

export default App;

