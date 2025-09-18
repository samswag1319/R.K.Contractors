# Create the Hero component
hero_component = """import React from 'react';
import { useScrollToSection } from '../hooks/useScrollToSection';

const Hero = () => {
  const scrollToSection = useScrollToSection();

  return (
    <section id="home" className="hero">
      <div className="container">
        <div className="hero__content">
          <h1 className="hero__title">Professional Painting & Polishing Services</h1>
          <p className="hero__subtitle">
            Transform your space with R.K.Contractors - Expert craftsmanship, reliable service, competitive pricing
          </p>
          <div className="hero__actions">
            <button
              className="btn btn--primary btn--lg"
              onClick={() => scrollToSection('contact')}
            >
              Get Free Quote
            </button>
            <button
              className="btn btn--outline btn--lg"
              onClick={() => scrollToSection('gallery')}
            >
              View Our Work
            </button>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Hero;"""

with open('src/components/Hero.js', 'w') as f:
    f.write(hero_component)

print("Created src/components/Hero.js")