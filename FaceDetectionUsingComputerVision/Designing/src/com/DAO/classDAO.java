package com.DAO;

import java.util.List;

import org.hibernate.Query;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import com.VO.classVO;


@Repository
public class classDAO
{
	@Autowired
	SessionFactory sessionfactory;
	
	public void insertclass(classVO vo)
	{
		Session session = sessionfactory.openSession();
		Transaction tr = session.beginTransaction();
		session.save(vo);
		tr.commit();
	}
	
	public List searchclass(classVO v) 
	{
		Session session = sessionfactory.openSession();
		Query q = session.createQuery("from classVO");
		List classls=q.list();
		return classls;
	}

}
