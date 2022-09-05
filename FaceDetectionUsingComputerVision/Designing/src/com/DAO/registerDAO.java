package com.DAO;

import java.util.List;

import org.hibernate.Query;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import com.VO.classVO;
import com.VO.registerVO;

@Repository
public class registerDAO
{

	@Autowired
	SessionFactory sessionfactory;
	
	public void insert(registerVO vo)
	{
		Session session = sessionfactory.openSession();
		Transaction tr = session.beginTransaction();
		session.save(vo);
		tr.commit();
	}
	
	public List searchStudent(registerVO v) 
	{
		Session session = sessionfactory.openSession();
		Query q = session.createQuery("from registerVO");
		List ls=q.list();
		return ls;
	}
	
}
