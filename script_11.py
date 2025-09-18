# Create the Process component
process_component = """import React from 'react';
import { appData } from '../data/appData';

const Process = () => {
  return (
    <section className="process">
      <div className="container">
        <div className="section__header">
          <h2>Our Work Process</h2>
          <p>From consultation to completion - here's how we deliver excellence</p>
        </div>
        <div className="process__steps" id="process-steps">
          {appData.process.map((step) => (
            <div key={step.step} className="process__step">
              <div className="step__number">{step.step}</div>
              <div className="step__content">
                <h3 className="step__title">{step.title}</h3>
                <p className="step__description">{step.description}</p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Process;"""

with open('src/components/Process.js', 'w') as f:
    f.write(process_component)

print("Created src/components/Process.js")