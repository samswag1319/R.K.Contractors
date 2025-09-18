import React from 'react';

const Gallery = () => {
  const galleryItems = [
    { icon: "🏠", title: "Interior Painting Project" },
    { icon: "🏗️", title: "Exterior Painting Project" },
    { icon: "🪵", title: "Wood Polishing Project" },
    { icon: "🪑", title: "Furniture Polishing" },
    { icon: "💧", title: "Waterproofing Project" },
    { icon: "🎨", title: "Texture Painting" }
  ];

  return (
    <section id="gallery" className="gallery">
      <div className="container">
        <div className="section__header">
          <h2>Our Portfolio</h2>
          <p>See the quality of our work in these completed projects</p>
        </div>
        <div className="gallery__placeholder">
          {galleryItems.map((item, index) => (
            <div key={index} className="gallery__item">
              <div className="gallery__image-placeholder">
                <span>{item.icon}</span>
                <p>{item.title}</p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Gallery;