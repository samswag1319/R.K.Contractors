# Create the Services component
services_component = """import React from 'react';
import { appData } from '../data/appData';
import { useScrollToSection } from '../hooks/useScrollToSection';

const Services = () => {
  const scrollToSection = useScrollToSection();

  return (
    <section id="services" className="services">
      <div className="container">
        <div className="section__header">
          <h2>Our Services</h2>
          <p>We provide comprehensive painting and polishing solutions for residential and commercial properties</p>
        </div>
        <div className="services__grid" id="services-grid">
          {appData.services.map((service) => (
            <div key={service.id} className="service__card">
              <span className="service__icon">{service.icon}</span>
              <h3 className="service__title">{service.title}</h3>
              <p className="service__description">{service.description}</p>
              <a
                href="#contact"
                className="service__link"
                onClick={(e) => {
                  e.preventDefault();
                  scrollToSection('contact');
                }}
              >
                Get Quote →
              </a>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Services;"""

with open('src/components/Services.js', 'w') as f:
    f.write(services_component)

print("Created src/components/Services.js")