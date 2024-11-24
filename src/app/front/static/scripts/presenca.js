document.addEventListener("DOMContentLoaded", function () {
  fetch('/static/scripts/presenca.json') // Caminho do arquivo JSON gerado
      .then(response => {
          if (!response.ok) {
              throw new Error('Erro ao carregar o arquivo JSON');
          }
          return response.json();
      })
      .then(data => {
          const anos = ['2021', '2022', '2023', '2024'];
          const presencas = anos.map(ano =>
              data.find(item => item.freq_situacao === 'Presente' && item.freq_ano == ano)?.freq_quantidade || 0
          );
          const faltas = anos.map(ano =>
              data.find(item => item.freq_situacao === 'Falta' && item.freq_ano == ano)?.freq_quantidade || 0
          );
          const faltasJustificadas = anos.map(ano =>
              data.find(item => item.freq_situacao === 'Falta Justificada' && item.freq_ano == ano)?.freq_quantidade || 0
          );

          const ctx = document.getElementById('presenca').getContext('2d');
          new Chart(ctx, {
              type: 'bar',
              data: {
                  labels: anos,
                  datasets: [
                      {
                          label: 'Presença',
                          data: presencas,
                          backgroundColor: 'green',
                          borderColor: 'black',
                          borderWidth: 1.5,
                      },
                      {
                          label: 'Faltas',
                          data: faltas,
                          backgroundColor: 'red',
                          borderColor: 'black',
                          borderWidth: 1.5,
                      },
                      {
                          label: 'Faltas Justificadas',
                          data: faltasJustificadas,
                          backgroundColor: 'blue',
                          borderColor: 'black',
                          borderWidth: 1.5,
                      },
                  ],
              },
              options: {
                  responsive: true,
                  animation: {
                      duration: 2000,
                      easing: 'easeOutBounce',
                  },
                  plugins: {
                      title: {
                          display: true,
                          text: 'Gráfico de Presença',
                          font: {
                              size: 18,
                              weight: 'bold',
                          },
                          color: '#333',
                      },
                  },
                  scales: {
                      y: {
                          beginAtZero: true,
                      },
                      x: {
                          barPercentage: 0.5,
                          categoryPercentage: 0.5,
                      },
                  },
              },
          });
      })
      .catch(error => console.error('Erro ao carregar o JSON:', error));
});
