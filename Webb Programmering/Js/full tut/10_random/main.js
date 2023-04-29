List = []
function Check() {
    high = document.getElementById("highest").value
    console.log(high)

for (i = 0; i<5; i+=1) {
    let x = +Math.random()*(high-1)+1
    console.log(x)
    List[List.length] = ("<li> "+ x+ " </li>")
   
}
console.log(List[0])
console.log(List.length)

List = List.replace(",", "")
document.getElementById("list").innerHTML = List

}
