/** 목록 추가 버튼을 눌렀을 경우 */
function OnTouchAddItemBtn() {
	/*
	document 객체는 웹 문서 최상단에 위치하는 객체를 의미한다. (즉, 웹 문서에 정의되는 모든 태그와 속성은 document 객체 하위에 존재한다는 것을
	알 수 있다.
	*/
	var oListItem = document.createElement("li");
	oListItem.appendChild(document.createTextNode("Hello, World!"));

	var oCommentList = document.getElementById("CommentList");

	/*
	appendChild 함수를 활용하면 특정 요소 하위에 새로운 요소를 추가하는 것이 가능하다. (즉, 해당 함수를 활용하면 동적으로 웹 문서의 구조를
	변경하는 것이 가능하다.)
	*/
	oCommentList.appendChild(oListItem);
}
