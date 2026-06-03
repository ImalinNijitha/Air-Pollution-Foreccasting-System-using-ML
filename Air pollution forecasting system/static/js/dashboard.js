// Auto-refresh sensor data every 30 seconds on factory_owner and worker views
const REFRESH_INTERVAL = 30 * 1000;

function pollReadings(factoryId) {
  fetch(`/api/factories/${factoryId}/readings`)
    .then(r => r.json())
    .then(data => {
      if (!data.length) return;
      const latest = data[0];
      // Update any sensor-value spans that have data-field attributes
      document.querySelectorAll("[data-field]").forEach(el => {
        const field = el.dataset.field;
        if (latest[field] !== undefined) {
          el.textContent = latest[field];
        }
      });
    })
    .catch(err => console.warn("Polling error:", err));
}

const factoryEl = document.querySelector("[data-factory-id]");
if (factoryEl) {
  const fid = factoryEl.dataset.factoryId;
  setInterval(() => pollReadings(fid), REFRESH_INTERVAL);
}
