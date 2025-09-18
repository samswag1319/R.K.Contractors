# Create the Testimonials component
testimonials_component = """import React, { useState, useEffect } from 'react';
import { appData } from '../data/appData';

const Testimonials = () => {
  const [currentTestimonial, setCurrentTestimonial] = useState(0);

  const nextTestimonial = () => {
    setCurrentTestimonial((prev) => (prev + 1) % appData.testimonials.length);
  };

  const prevTestimonial = () => {
    setCurrentTestimonial((prev) => 
      prev === 0 ? appData.testimonials.length - 1 : prev - 1
    );
  };

  useEffect(() => {
    const interval = setInterval(nextTestimonial, 5000);
    return () => clearInterval(interval);
  }, []);

  const testimonial = appData.testimonials[currentTestimonial];

  return (
    <section className="testimonials">
      <div className="container">
        <div className="section__header">
          <h2>What Our Clients Say</h2>
          <p>Real feedback from satisfied customers</p>
        </div>
        <div className="testimonials__carousel" id="testimonials-carousel">
          <div className="testimonial__card active">
            <div className="testimonial__rating">
              {[...Array(testimonial.rating)].map((_, index) => (
                <span key={index}>⭐</span>
              ))}
            </div>
            <blockquote className="testimonial__review">
              "{testimonial.review}"
            </blockquote>
            <div className="testimonial__author">
              <h4>{testimonial.name}</h4>
              <p>{testimonial.project}</p>
            </div>
          </div>
        </div>
        <div className="testimonials__controls">
          <button 
            className="carousel__btn carousel__btn--prev" 
            onClick={prevTestimonial}
          >
            ‹
          </button>
          <button 
            className="carousel__btn carousel__btn--next" 
            onClick={nextTestimonial}
          >
            ›
          </button>
        </div>
      </div>
    </section>
  );
};

export default Testimonials;"""

with open('src/components/Testimonials.js', 'w') as f:
    f.write(testimonials_component)

print("Created src/components/Testimonials.js")