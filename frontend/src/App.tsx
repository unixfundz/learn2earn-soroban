const cards = [
  {
    title: "For companies",
    description: "Onboard new devs with milestone-based token rewards"
  },
  {
    title: "For DAOs",
    description: "Fund community education with verifiable outcomes"
  },
  {
    title: "For teachers",
    description: "Incentivize students with micro-rewards per module"
  },
  {
    title: "For mentors",
    description: "Back a mentee's journey with real on-chain commitment"
  }
];

export function App() {
  return (
    <main className="container">
      <header>
        <p className="eyebrow">Learn2Earn Soroban</p>
        <h1>Learn. Earn. On-chain.</h1>
        <p>
          Create quests, fund milestones, verify progress, and release token rewards on Stellar Soroban.
        </p>
      </header>

      <section>
        <h2>How it works</h2>
        <ol>
          <li>Create Quest</li>
          <li>Fund Quest</li>
          <li>Learn + Submit Proof</li>
          <li>Verify + Earn</li>
        </ol>
      </section>

      <section className="grid">
        {cards.map((card) => (
          <article key={card.title} className="card">
            <h3>{card.title}</h3>
            <p>{card.description}</p>
          </article>
        ))}
      </section>
    </main>
  );
}

