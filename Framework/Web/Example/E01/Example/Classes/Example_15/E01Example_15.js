/** 회원 버튼을 눌렀을 경우 */
function OnTouchMemberShipBtn(a_bIsJoin) {
	// 회원 가입 상태 일 경우
	if(a_bIsJoin) {
		HandleJoinState();
	} else {
		HandleClearState();
	}
}

/** 가입 상태를 처리한다 */
function HandleJoinState() {
	var oID = document.getElementById("ID");
	var oPassword = document.getElementById("Password");

	// 입력 필드가 유효하지 않을 경우
	if(oID.value.length <= 0 || oPassword.value.length <= 0) {
		alert("아이디 or 비밀번호를 입력해주세요.");
	} else {
		/*
		localStorage 객체를 활용하면 반영구적으로 데이터를 저장하는 것이 가능하다. (즉, 해당 객체에 저장 된 데이터는 명시적으로 제거하지 않는 이상
		계속 유지가 된다는 것을 알 수 있다.)

		단, localStorage 객체는 데이터를 웹 브라우저에 저장하기 때문에 저장 된 데이터가 웹 브라우저 별로 다를 수 있다는 것을 알 수 있다.
		*/
		var oSavedID = localStorage.getItem("ID");
		var oSavedPassword = localStorage.getItem("Password");

		// 아이디가 존재 할 경우
		if(oSavedID == oID.value) {
			alert("아이디가 존재합니다.");
		} else {
			localStorage.setItem("ID", oID.value);
			localStorage.setItem("Password", oPassword.value);

			alert("회원 가입에 성공했습니다.");
		}
	}
}

/** 지우기 상태를 처리한다 */
function HandleClearState() {
	localStorage.clear();
}
