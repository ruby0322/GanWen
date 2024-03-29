const copy = () => {
    document.querySelector('#output').select();
    document.execCommand('Copy');
};

const displayConverted = data => {
    const converted = data['converted'];
    document.querySelector('#output').value = converted;
    document.querySelector('#output').innerHTML = converted;
};

const fetchGanTextAPI = async toConvert => {
    apiUrl = `https://ganwenapi.herokuapp.com/gan_text?to_convert=${toConvert}`;

    fetch(apiUrl)
    .then(response => response.json())
    .then(data => displayConverted(data));
};

const convert = async () => {
    const toConvert = document.querySelector('#input').value.replaceAll('\n', '[[endl]]');
    console.log(toConvert);
    if (toConvert.length > 0)
        fetchGanTextAPI(toConvert);
    else
        fetchGanTextAPI('哇，你什麼都沒放，還想要我加入什麼幹元素，你很聰明欸。');
};

const resetInput = () => {
    console.log('dawdaw');
    document.querySelector('#input').value = '';
    document.querySelector('#input').innerHTML = '';
    convert();
};

const setInput = text => {
    document.querySelector('#input').value = text;
    document.querySelector('#input').innerHTML = text;
    return text;
};

const randWiki = async () => {
    apiUrl = 'https://ganwenapi.herokuapp.com/rand_wiki';

    fetch(apiUrl)
    .then(response => response.json())
    .then(data => data['content'])
    .then(text => setInput(text))
    .then(text => fetchGanTextAPI(text));
};

const bullshit = async len => {
    apiUrl = 'https://ganwenapi.herokuapp.com/bs';
    params = `?topic=${document.querySelector('#input').value}&len=${len}`;
    fetch(apiUrl+params)
    .then(response => response.json())
    .then(data => data['bullshit'])
    .then(text => fetchGanTextAPI(text));
};