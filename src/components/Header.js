import React, { useState } from 'react';
import { useScrollToSection } from '../hooks/useScrollToSection';

const Header = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const scrollToSection = useScrollToSection();

  const handleNavClick = (sectionId) => {
    scrollToSection(sectionId);
    setIsMenuOpen(false);
  };

  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen);
  };

  return (
    <header className="header">
      <nav className="nav container">
        <div className="nav__brand">
          <h2>R.K.Contractors</h2>
        </div>
        <ul className={`nav__menu ${isMenuOpen ? 'active' : ''}`} id="nav-menu">
          <li>
            <a
              href="#home"
              className="nav__link"
              onClick={(e) => {
                e.preventDefault();
                handleNavClick('home');
              }}
            >
              Home
            </a>
          </li>
          <li>
            <a
              href="#services"
              className="nav__link"
              onClick={(e) => {
                e.preventDefault();
                handleNavClick('services');
              }}
            >
              Services
            </a>
          </li>
          <li>
            <a
              href="#gallery"
              className="nav__link"
              onClick={(e) => {
                e.preventDefault();
                handleNavClick('gallery');
              }}
            >
              Gallery
            </a>
          </li>
          <li>
            <a
              href="#about"
              className="nav__link"
              onClick={(e) => {
                e.preventDefault();
                handleNavClick('about');
              }}
            >
              About Us
            </a>
          </li>
          <li>
            <a
              href="#contact"
              className="nav__link"
              onClick={(e) => {
                e.preventDefault();
                handleNavClick('contact');
              }}
            >
              Contact
            </a>
          </li>
        </ul>
        <div className="nav__actions">
          <span className="nav__phone">+91 91309 89096</span>
          <button
            className="btn btn--primary"
            onClick={() => scrollToSection('contact')}
          >
            Get Free Quote
          </button>
        </div>
        <button
          className={`nav__toggle ${isMenuOpen ? 'active' : ''}`}
          id="nav-toggle"
          onClick={toggleMenu}
        >
          <span></span>
          <span></span>
          <span></span>
        </button>
      </nav>
    </header>
  );
};

export default Header;