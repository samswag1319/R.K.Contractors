# Create the WhyChooseUs component
why_choose_us_component = """import React from 'react';
import { appData } from '../data/appData';

const WhyChooseUs = () => {
  return (
    <section id="about" className="why-choose-us">
      <div className="container">
        <div className="section__header">
          <h2>Why Choose R.K.Contractors?</h2>
          <p>We're committed to delivering exceptional results with every project</p>
        </div>
        <div className="features__grid" id="features-grid">
          {appData.whyChooseUs.map((feature, index) => (
            <div key={index} className="feature__card">
              <span className="feature__icon">{feature.icon}</span>
              <h3 className="feature__title">{feature.title}</h3>
              <p className="feature__description">{feature.description}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default WhyChooseUs;"""

with open('src/components/WhyChooseUs.js', 'w') as f:
    f.write(why_choose_us_component)

print("Created src/components/WhyChooseUs.js")