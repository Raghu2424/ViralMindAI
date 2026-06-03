import { useState } from "react";

function App() {
  const [topic, setTopic] = useState("");
  const [result, setResult] = useState("");
  const [endpoint, setEndpoint] = useState("generate-linkedin");

  const generatePost = async () => {
    const response = await fetch(
      `http://127.0.0.1:8000/${endpoint}`,
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ topic }),
      }
    );

    const data = await response.json();

    setResult(
      data.linkedin_post ||
      data.caption ||
      data.reel_script ||
      data.ideas
    );
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>🚀 ViralMind AI</h1>

      <p>
        Generate LinkedIn posts, Instagram captions,
        Reel scripts and viral ideas using AI.
      </p>

      <div>
        <button onClick={() => setEndpoint("generate-linkedin")}>
          LinkedIn
        </button>

        <button onClick={() => setEndpoint("generate-instagram")}>
          Instagram
        </button>

        <button onClick={() => setEndpoint("generate-reel")}>
          Reel
        </button>

        <button onClick={() => setEndpoint("viral-ideas")}>
          Viral Ideas
        </button>
      </div>

      <br />

      <input
        type="text"
        placeholder="Enter Topic"
        value={topic}
        onChange={(e) => setTopic(e.target.value)}
      />

      <button onClick={generatePost}>
        Generate Content
      </button>

      <br /><br />

      <textarea
        rows="15"
        cols="80"
        value={result}
        readOnly
      />

      <br />

      <button
        onClick={() => navigator.clipboard.writeText(result)}
      >
        Copy Output
      </button>
    </div>
  );
}

export default App;
