package com.VO;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name="classmaster")
public class classVO
{
	@Id
	@GeneratedValue(strategy=GenerationType.AUTO)
	@Column(name="classId")
	private int classId;
	
	@Column(name="className")
	private String className;
	
	public int getclassId() {
		return classId;
	}

	public void setclassId(int classId) {
		this.classId = classId;
	}

	public String getclassName() {
		return className;
	}

	public void setclassName(String className) {
		this.className = className;
	}

	/*public String getclassDepartment() {
		return classDepartment;
	}

	public void setclassDepartment(String classDepartment) {
		this.classDepartment = classDepartment;
	}

	@Column(name="classDepartment")
	private String classDepartment;
*/
	}
