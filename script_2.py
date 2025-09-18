# Create the data file (equivalent to appData from app.js)
app_data = """export const appData = {
  companyInfo: {
    name: "R.K.Contractors",
    tagline: "Professional Painting & Polishing Services",
    phone: "+91 98765 43210",
    email: "info@rkcontractors.com",
    address: "123 Business District, Mumbai, Maharashtra 400001",
    hours: "Mon-Sat: 8:00 AM - 6:00 PM"
  },
  services: [
    {
      id: 1,
      title: "Interior Painting",
      description: "Transform your indoor spaces with premium quality paints and expert application techniques.",
      icon: "🏠"
    },
    {
      id: 2,
      title: "Exterior Painting",
      description: "Protect and beautify your property's exterior with weather-resistant paints and professional finishes.",
      icon: "🏗️"
    },
    {
      id: 3,
      title: "Wood Polishing",
      description: "Expert PU, Melamine, and Duco finishes for doors, furniture, and wooden surfaces.",
      icon: "🪵"
    },
    {
      id: 4,
      title: "Furniture Polishing",
      description: "Restore and enhance your furniture with professional polishing and refinishing services.",
      icon: "🪑"
    },
    {
      id: 5,
      title: "Waterproofing",
      description: "Comprehensive waterproofing solutions to protect your property from moisture and leaks.",
      icon: "💧"
    },
    {
      id: 6,
      title: "Texture Painting",
      description: "Create stunning decorative finishes with artistic texture painting techniques.",
      icon: "🎨"
    }
  ],
  whyChooseUs: [
    {
      title: "10+ Years Experience",
      description: "Proven track record of successful projects",
      icon: "⭐"
    },
    {
      title: "Licensed & Insured",
      description: "Fully licensed and insured for your peace of mind",
      icon: "🛡️"
    },
    {
      title: "Quality Materials",
      description: "We use only premium paints and materials",
      icon: "🏆"
    },
    {
      title: "Timely Completion",
      description: "Projects completed on schedule, every time",
      icon: "⏰"
    },
    {
      title: "Competitive Pricing",
      description: "Fair and transparent pricing with no hidden costs",
      icon: "💰"
    },
    {
      title: "Professional Team",
      description: "Skilled craftsmen dedicated to excellence",
      icon: "👥"
    }
  ],
  testimonials: [
    {
      id: 1,
      name: "Priya Sharma",
      project: "Interior Painting",
      rating: 5,
      review: "Excellent work quality and professional service. R.K.Contractors transformed our home beautifully!"
    },
    {
      id: 2,
      name: "Rajesh Kumar",
      project: "Exterior Painting",
      rating: 5,
      review: "Very satisfied with the exterior painting work. The team was punctual and delivered exactly what was promised."
    },
    {
      id: 3,
      name: "Sunita Patel",
      project: "Wood Polishing",
      rating: 5,
      review: "Amazing wood polishing service. Our furniture looks brand new. Highly recommend R.K.Contractors!"
    }
  ],
  process: [
    {
      step: 1,
      title: "Free Consultation & Quote",
      description: "We assess your project requirements and provide a detailed, no-obligation quote."
    },
    {
      step: 2,
      title: "Surface Preparation",
      description: "Thorough cleaning and preparation of surfaces for optimal paint adhesion."
    },
    {
      step: 3,
      title: "Premium Materials Selection",
      description: "We recommend and use only high-quality paints and materials for lasting results."
    },
    {
      step: 4,
      title: "Professional Application",
      description: "Expert application using proper techniques and professional equipment."
    },
    {
      step: 5,
      title: "Quality Inspection",
      description: "Detailed quality check to ensure every aspect meets our high standards."
    },
    {
      step: 6,
      title: "Final Walkthrough",
      description: "Complete walkthrough with you to ensure 100% satisfaction with the completed work."
    }
  ]
};"""

with open('src/data/appData.js', 'w') as f:
    f.write(app_data)

print("Created src/data/appData.js")