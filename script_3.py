# Create utility hooks
scroll_hook = """import { useCallback } from 'react';

export const useScrollToSection = () => {
  const scrollToSection = useCallback((sectionId) => {
    const section = document.getElementById(sectionId);
    if (section) {
      const headerHeight = document.querySelector('.header')?.offsetHeight || 80;
      const sectionTop = section.offsetTop - headerHeight - 20;
      window.scrollTo({
        top: sectionTop,
        behavior: 'smooth'
      });
    }
  }, []);

  return scrollToSection;
};"""

with open('src/hooks/useScrollToSection.js', 'w') as f:
    f.write(scroll_hook)

print("Created src/hooks/useScrollToSection.js")