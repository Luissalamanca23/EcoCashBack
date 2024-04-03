const { getLighthouseStats } = require('@vercel/speed-insights');

async function obtenerInsightsDeVelocidad(url) {
  try {
    const stats = await getLighthouseStats(url);
    console.log(stats);
    // Puedes hacer lo que quieras con los resultados aquí
  } catch (error) {
    console.error('Error al obtener los insights de velocidad:', error);
  }
}

// Llamar a la función con la URL de tu sitio web
obtenerInsightsDeVelocidad('ecocashback.vercel.app');
