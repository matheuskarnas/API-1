var ctx = document.getElementById('posicionamento').getContext('2d') // Alterar o 'Meu grafico' para o que quer colocar na id

var posicionamento = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ['2021', '2022', '2023', '2024'], // Rótulos do eixo X
    datasets: [
      {
        label: 'Presença',
        data: [64, 79, 83, 83], // Valores para o Produto 1
        backgroundColor: 'green',
        borderColor: 'black',
        borderWidth: 1.5,
      },
      {
        label: 'Faltas',
        data: [0, 0, 0, 1], // Valores para o Produto 2
        backgroundColor: 'red',
        borderColor: 'black',
        borderWidth: 1.5,
      },
      {
        label: 'Faltas Justificadas',
        data: [6, 1, 1, 2], // Valores para o Produto 3
        backgroundColor: 'blue',
        borderColor: 'black',
        borderWidth: 1.5,
      },
    ],
  },
  options: {
    responsive: true,
    animation: {
      duration: 1500, // Duração da animação em milissegundos
      easing: 'easeOutBounce', // Tipo de animação
    },
    plugins: {
      title: {
        display: true,
        text: '', // Texto do título
        font: {
          size: 18,
          weight: 'bold',
          family: 'Arial',
        },
        color: '#333',
        padding: {
          top: 20,
          bottom: 10,
        },
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
})
