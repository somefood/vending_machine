let money = 0;
const insert = document.querySelector('#insert');
insert.addEventListener('click', function(e){
    console.log("hello");
    money = prompt('얼마를 넣으십니까?');
    money = parseInt(money);
    if (isNaN(money)){
        alert("숫자만 입력해주세요.")
        return 0;
    }
    if (money % 10 === 0) {
        document.querySelector('.print-money').innerHTML = String(money);
        const qts = document.querySelectorAll('.quantity')
        // ES6 버전으로 한번 작성해보
        Array.from(qts, x => {
            x.style.color = "red";
        })
    } else {
        alert("10원 단위로 입력해주세요.");
    }
})

const refund = document.querySelector('#refund');
refund.addEventListener('click', function(e){
    const currency_list =  [5000, 1000, 500, 100, 50, 10];
    let refund_list = []
    for(let i=0; i<currency_list.length; i++){
        refund_list[i] = Math.floor(money / currency_list[i])
        money %= currency_list[i]
        document.querySelector('.print-money').innerHTML = String(money);
    }
    console.log(refund_list)
    const return_area = document.querySelector("#return-area");
    return_area.innerHTML = "";
    for (let i=0; i<currency_list.length; i++) {
        for (let j=0; j<refund_list[i]; j++){
            let currency = currency_list[i]
            let newDiv = document.createElement("div");
            if (currency >= 1000) newDiv.className = `paper money-${currency}`;
            else newDiv.className = `coin money-${currency}`;
            newDiv.innerHTML = String(currency);
            return_area.append(newDiv);
        }
    }
    const qts = document.querySelectorAll('.quantity')
    // ES6 버전으로 한번 작성해보
    Array.from(qts, x => {
        x.style.color = "black";
    })
});

let items = document.querySelectorAll('.beverage');
Array.from(items).forEach(function(item){
    item.addEventListener('click', function(e){
        let target = e.currentTarget;
        let item_pk = target.dataset.id;
        let item_price = parseInt(target.innerHTML);
        let quantity = target.previousElementSibling;
        if (money === 0) {
            alert("돈을 넣어주세요.");
            return 0;
        } else if (money < item_price) {
            alert("돈이 부족합니다.");
            return 0;
        } else if (quantity.innerHTML.trim() === 'X') {
            alert('재고가 없습니다.')
            return 0;
        } else {
            const select =  confirm("구입하시겠습니까?");
            if (select){
                money -= item_price;
                document.querySelector('.print-money').innerHTML = String(money);
                saveQuantity(target, item_pk);
            }
        }
    })
});

function saveQuantity(target, pk) {
    const url = myGlobal.item_url.replace(1, pk);
    $.ajax({
        url: url,
        method: 'POST',
        data: {
            csrfmiddlewaretoken: myGlobal.csrfmiddlewaretoken
        },
        success: function(response) {
            if (response.quantity <=0 ){
                target.previousElementSibling.innerHTML = "X";
            }
        }
    })
}