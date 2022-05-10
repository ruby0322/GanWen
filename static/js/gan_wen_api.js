const copy = () => {
    document.querySelector('#output').select();
    document.execCommand('Copy');
};
const displayConverted = data => {
    const converted = data['converted'];
    document.querySelector('#output').value = converted;
    document.querySelector('#output').innerHTML = converted;
    console.log(converted);
};
const fetchGanTextAPI = async toConvert => {
    apiUrl = `https://ganwenapi.herokuapp.com/gan_text?to_convert=${toConvert}`;

    fetch(apiUrl)
    .then(response => response.json())
    .then(data => displayConverted(data));
};
const convert = async () => {
    const toConvert = document.querySelector('#input').value;
    console.log(toConvert);
    fetchGanTextAPI(toConvert);
};