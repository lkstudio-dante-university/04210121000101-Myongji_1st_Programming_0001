/** 회원 */
class CP01Member_08 {
	m_oID = "";
	m_oPassword = "";
	m_nGender = 0;
	m_oCommentList = [];

	/** 생성자 */
	constructor(a_oID, a_oPassword, m_nGender) {
		this.m_oID = a_oID;
		this.m_oPassword = a_oPassword;
		this.m_nGender = a_nGender;
	}
}
