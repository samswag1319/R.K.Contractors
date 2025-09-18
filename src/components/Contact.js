import React, { useState } from 'react';

const Contact = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    phone: '',
    service: '',
    message: ''
  });
  const [isLoading, setIsLoading] = useState(false);
  const [showSuccess, setShowSuccess] = useState(false);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true);

    // Simulate form submission
    setTimeout(() => {
      setIsLoading(false);
      setShowSuccess(true);
      setFormData({
        name: '',
        email: '',
        phone: '',
        service: '',
        message: ''
      });
    }, 2000);
  };

  const closeSuccessMessage = () => {
    setShowSuccess(false);
  };

  return (
    <>
      <section id="contact" className="contact">
        <div className="container">
          <div className="section__header">
            <h2>Get Your Free Quote Today</h2>
            <p>Ready to transform your space? Contact us for a free consultation</p>
          </div>
          <div className="contact__content">
            <div className="contact__form-wrapper">
              <form className="contact__form" onSubmit={handleSubmit}>
                <div className="form-group">
                  <label htmlFor="name" className="form-label">Full Name *</label>
                  <input
                    type="text"
                    id="name"
                    name="name"
                    className="form-control"
                    value={formData.name}
                    onChange={handleInputChange}
                    required
                  />
                </div>
                <div className="form-group">
                  <label htmlFor="email" className="form-label">Email Address *</label>
                  <input
                    type="email"
                    id="email"
                    name="email"
                    className="form-control"
                    value={formData.email}
                    onChange={handleInputChange}
                    required
                  />
                </div>
                <div className="form-group">
                  <label htmlFor="phone" className="form-label">Phone Number *</label>
                  <input
                    type="tel"
                    id="phone"
                    name="phone"
                    className="form-control"
                    value={formData.phone}
                    onChange={handleInputChange}
                    required
                  />
                </div>
                <div className="form-group">
                  <label htmlFor="service" className="form-label">Service Required *</label>
                  <select
                    id="service"
                    name="service"
                    className="form-control"
                    value={formData.service}
                    onChange={handleInputChange}
                    required
                  >
                    <option value="">Select a service</option>
                    <option value="interior-painting">Interior Painting</option>
                    <option value="exterior-painting">Exterior Painting</option>
                    <option value="wood-polishing">Wood Polishing</option>
                    <option value="furniture-polishing">Furniture Polishing</option>
                    <option value="waterproofing">Waterproofing</option>
                    <option value="texture-painting">Texture Painting</option>
                  </select>
                </div>
                <div className="form-group">
                  <label htmlFor="message" className="form-label">Project Description *</label>
                  <textarea
                    id="message"
                    name="message"
                    className="form-control"
                    rows="4"
                    value={formData.message}
                    onChange={handleInputChange}
                    placeholder="Please describe your project requirements, area size, timeline, etc."
                    required
                  />
                </div>
                <button type="submit" className="btn btn--primary btn--full-width" disabled={isLoading}>
                  {isLoading ? 'Sending...' : 'Send Quote Request'}
                </button>
              </form>
            </div>
            <div className="contact__info">
              <div className="contact__item">
                <h4>📞 Phone</h4>
                <p><a href="tel:+919130989096">+91 91309 89096</a></p>
              </div>
              <div className="contact__item">
                <h4>✉️ Email</h4>
                <p><a href="mailto:info@rkcontractors.com">info@rkcontractors.com</a></p>
              </div>
              <div className="contact__item">
                <h4>📍 Address</h4>
                <p>123 Business District<br />Vasai, Palghar, Maharashtra 401202</p>
              </div>
              <div className="contact__item">
                <h4>🕒 Hours</h4>
                <p>Mon-Sat: 8:00 AM - 6:00 PM<br />Sunday: Closed</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Loading Overlay */}
      {isLoading && (
        <div className="loading-overlay">
          <div className="loading-spinner"></div>
          <p>Sending your quote request...</p>
        </div>
      )}

      {/* Success Message */}
      {showSuccess && (
        <div className="success-message">
          <div className="success-content">
            <h3>✅ Quote Request Sent!</h3>
            <p>Thank you for contacting R.K.Contractors. We'll get back to you within 24 hours with a detailed quote.</p>
            <button className="btn btn--primary" onClick={closeSuccessMessage}>
              Close
            </button>
          </div>
        </div>
      )}
    </>
  );
};

export default Contact;