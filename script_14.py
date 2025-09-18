# Create the main App.js component
app_component = """import React, { useEffect } from 'react';
import Header from './components/Header';
import Hero from './components/Hero';
import Services from './components/Services';
import Gallery from './components/Gallery';
import WhyChooseUs from './components/WhyChooseUs';
import Testimonials from './components/Testimonials';
import Process from './components/Process';
import Contact from './components/Contact';
import Footer from './components/Footer';
import './styles/App.css';

function App() {
  useEffect(() => {
    // Initialize scroll effects and other DOM interactions
    const setupScrollEffects = () => {
      const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
      };

      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('animate-in');
          }
        });
      }, observerOptions);

      // Observe all sections
      const sections = document.querySelectorAll('section');
      sections.forEach(section => {
        observer.observe(section);
      });

      return () => observer.disconnect();
    };

    const cleanup = setupScrollEffects();
    return cleanup;
  }, []);

  return (
    <div className="App">
      <Header />
      <main>
        <Hero />
        <Services />
        <Gallery />
        <WhyChooseUs />
        <Testimonials />
        <Process />
        <Contact />
      </main>
      <Footer />
    </div>
  );
}

export default App;"""

with open('src/App.js', 'w') as f:
    f.write(app_component)

print("Created src/App.js")