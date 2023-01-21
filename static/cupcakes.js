$('#cupcake-form').on('submit', async (e) => {
  e.preventDefault();
  await addCupcake();
  loadCupcakes();
  completeForm();
})

async function addCupcake() {
  let flavor = $('#flavor-input').val();
  let rating = $('#rating-input').val();
  let size = $('#size-input').val();
  let image = $('#image-input').val();

  await axios.post(`/api/cupcakes`, {flavor,rating,size,image});
}

async function loadCupcakes() {
  $('ul').empty()
  let cupcakes = await axios.get(`/api/cupcakes`);

  for (let cupcake of cupcakes.data.cupcakes) {
      $('ul').append(`<li>${cupcake.flavor}</li>`)
  }
  console.log(cupcakes.data.cupcakes)
}

function completeForm() {
  let flavor = $('#flavor-input').val('');
  let rating = $('#rating-input').val('');
  let size = $('#size-input').val('');
  let image = $('#image-input').val('');
}

loadCupcakes();
  