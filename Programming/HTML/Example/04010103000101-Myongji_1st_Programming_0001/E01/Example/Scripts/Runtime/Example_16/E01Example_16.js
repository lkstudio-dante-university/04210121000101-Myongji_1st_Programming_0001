/** 회원 */
class CE01Member_16 {
	m_oID = "";
	m_oPassword = "";

	/** 생성자 */
	constructor(a_oID, a_oPassword) {
		this.m_oID = a_oID;
		this.m_oPassword = a_oPassword;
	}
}

/** 회원 추가 버튼을 눌렀을 경우 */
function OnTouchAddMemberBtn() {
	var oIDInput = document.getElementById("ID");
	var oPasswordInput = document.getElementById("Password");

	// 입력 필드가 유효하지 않을 경우
	if(oIDInput.value.length <= 0 || oPasswordInput.value.length <= 0) {
		alert("아이디 or 비밀번호를 입력해주세요.");
		return;
	}

	var oMember = new CE01Member_16(oIDInput.value, oPasswordInput.value);
	var oJSONStr = (localStorage.getItem("Members") != null) ? localStorage.getItem("Members") : "[]";
	
	/*
	JSON 객체를 활용하면 특정 데이터를 손쉽게 JSON 형식의 문자열로 변환하는 것이 가능하다.

	JSON.parse 함수는 JSON 형식의 문자열을 데이터로 변환하는 역할을 수행하며 JSON.stringify 함수는 데이터를 JSON 형식의 문자열로 
	변환하는 역할을 수행한다.  (즉, 해당 함수를 활용하면 배열을 비롯한 다양한 자료형의 데이터를 저장 및 로드하는 것이 가능하다.)

	JSON (Java Script Object Notation) 이란?
	- 문자열 기반의 데이터 포맷을 의미한다. (즉, Java Script 에서 객체를 데이터로 표현하기 위한 형식이라는 것을 알 수 있다.)

	JSON 은 배열을 비롯한 여러 데이터를 표현하는 것이 가능하기 때문에 현재 현업에서도 많이 활용되는 데이터 포맷이다. (즉, JSON 이외에도 
	CSV 와 같은 데이터 포맷이 존재한다는 것을 알 수 있다.)
	*/
	var oMemberList = JSON.parse(oJSONStr);
	oMemberList.push(oMember);

	oIDInput.value = "";
	oPasswordInput.value = "";

	localStorage.setItem("Members", JSON.stringify(oMemberList));
}

/** 모든 회원 보기 버튼을 눌렀을 경우 */
function OnTouchPrintAllMembersBtn() {
	/*
	window 객체의 location 속성을 활용하면 다른 웹 문서를 로드하는 것이 가능하다. (즉, 해당 속성은 HTML 의 a 태그와 유사하다는 것을 
	알 수 있다.)
	*/
	window.location.href = "./E01Members_16.html";
}
