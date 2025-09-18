import React from 'react';
import { useScrollToSection } from '../hooks/useScrollToSection';

const Footer = () => {
  const scrollToSection = useScrollToSection();

  const handleLinkClick = (sectionId) => (e) => {
    e.preventDefault();
    scrollToSection(sectionId);
  };

  return (
    <footer className="footer">
      <div className="container">
        <div className="footer__content">
          <div className="footer__section">
            <h3>R.K.Contractors</h3>
            <p>Professional painting and polishing services in Mumbai. Transform your space with quality craftsmanship and reliable service.</p>
            <div className="footer__social">
              <p>📞 <a href="tel:+919130989096">+91 91309 89096</a></p>
              <p>✉️ <a href="mailto:info@rkcontractors.com">info@rkcontractors.com</a></p>
            </div>
          </div>
          <div className="footer__section">
            <h4>Quick Links</h4>
            <ul>
              <li><a href="#home" onClick={handleLinkClick('home')}>Home</a></li>
              <li><a href="#services" onClick={handleLinkClick('services')}>Services</a></li>
              <li><a href="#gallery" onClick={handleLinkClick('gallery')}>Gallery</a></li>
              <li><a href="#contact" onClick={handleLinkClick('contact')}>Contact</a></li>
            </ul>
          </div>
          <div className="footer__section">
            <h4>Our Services</h4>
            <ul>
              <li>Interior Painting</li>
              <li>Exterior Painting</li>
              <li>Wood Polishing</li>
              <li>Furniture Polishing</li>
              <li>Waterproofing</li>
              <li>Texture Painting</li>
            </ul>
          </div>
          <div className="footer__section">
            <h4>Service Areas</h4>
            <ul>
              <li>Mumbai Central</li>
              <li>South Mumbai</li>
              <li>Western Suburbs</li>
              <li>Eastern Suburbs</li>
              <li>Navi Mumbai</li>
              <li>Thane</li>
            </ul>
          </div>
        </div>
        <div className="footer__bottom">
          <p>&copy; 2025 R.K.Contractors. All rights reserved. Licensed & Insured Painting Contractors in Mumbai.</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;