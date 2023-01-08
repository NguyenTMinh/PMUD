const detect_name = document.querySelector(".detect_name h1");
const search_img = document.querySelector(".search_img");
const detect_desc = document.querySelector(".body p");
const btn = document.querySelector("#button");

function detect() {
  fetch("http://localhost:5000")
    .then((res) => res.json())
    .then((data) => {
      console.log(data);
      fetch("http://localhost/client/server_php/apiGetAll.php")
        .then((res) => res.json())
        .then((res) => {
          console.log(res);

          for (let i = 0; i < res.length; i++) {
            if (res[i].id == data[data.length - 1]) {
              console.log(data[data.length - 1]);
              detect_name.innerHTML = `Đây là biển ${res[i].traffic_sign} , một vài hình ảnh tương tự bạn có thể tìm trên Bing.com `;
              search_img.src = ` https://www.bing.com/images/search?q=${res[i].traffic_sign}_traffic_sign&form=QBLH&sp=-1&pq=stop&sc=10-4&qs=n `;
              detect_desc.innerHTML = ` ${res[i].descripsion} `;
              search_img.hidden = false;
            }
          }
        })
        .catch((err) => {
          console.log(err);
        });
      let char = (detect_name.innerHTML = data.char);
      return data;
    })
    .catch((err) => {
      console.log(err);
    });
}
