<div class="trust-bar-container">
  <p class="trust-label">PREVIOUS LEADERSHIP & EXPERIENCE</p>
  <div class="trust-logos">
    <img src="/images/logos/ubx-logo.png" alt="UBX" class="trust-logo">
    <img src="/images/logos/unionbank-logo.png" alt="UnionBank" class="trust-logo">
    <img src="/images/logos/manulife-logo.png" alt="Manulife" class="trust-logo">
    <!--img src="/images/logos/maximus-logo.png" alt="Maximus" class="trust-logo"-->
    <!--img src="/images/logos/rogers-logo.png" alt="Rogers" class="trust-logo"-->
  </div>
</div>

<style>
  .trust-bar-container {
    margin: 2rem 0 3rem 0; /* Spacing above and below */
    text-align: center;
    opacity: 0.8;
  }

  .trust-label {
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 1.5rem;
    opacity: 0.6; /* Subtle label */
    font-weight: 600;
  }

  .trust-logos {
    display: flex;
    justify-content: center; /* Center align items */
    align-items: center;     /* Vertical center */
    flex-wrap: wrap;         /* Wrap to next line on mobile */
    gap: 3rem;               /* Space between logos */
  }

  .trust-logo {
    height: 35px;            /* Fixed height for consistency */
    width: auto;             /* Maintain aspect ratio */
    filter: grayscale(100%); /* Make them black/white */
    opacity: 0.6;            /* Make them subtle */
    transition: all 0.3s ease;
  }

  /* Hover Effect: Bring back color */
  .trust-logo:hover {
    filter: grayscale(0%);
    opacity: 1;
    transform: scale(1.05);
  }

  /* Mobile Tweaks */
  @media (max-width: 600px) {
    .trust-logos {
      gap: 1.5rem;
    }
    .trust-logo {
      height: 25px; /* Smaller on mobile */
    }
  }

  /* If the user is in dark mode, invert the colors to make black logos white */
  /* Dark Mode Handling - FIXED */
  /* We target the 'dark' class on the HTML tag */
  html.dark .trust-logo {
    filter: grayscale(100%) invert(1) brightness(10);
    opacity: 0.5;
  }
</style>