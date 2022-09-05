package com.controller;

import java.util.List;

import javax.servlet.http.HttpServletRequest;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.ModelAndView;

import com.DAO.classDAO;
import com.DAO.registerDAO;
import com.VO.classVO;
import com.VO.registerVO;

@Controller
public class controller
{
	@Autowired
	registerDAO dao;
	@Autowired
	classDAO classdao;
	

	
@RequestMapping(value ="/index.html", method = RequestMethod.GET)

	public ModelAndView indexLoad()
	{

		return new ModelAndView("Admin/index");
	}



@RequestMapping(value = "/addStudent.html", method = RequestMethod.GET)
	
	public ModelAndView registerLoad()
	{
	
		return new ModelAndView("Admin/addStudent", "register", new registerVO());
	}

@RequestMapping(value = "/registercontroller.html", method = RequestMethod.POST)
	public ModelAndView save(HttpServletRequest request, @ModelAttribute registerVO v) 
	{
			
		this.dao.insert(v);
		return new ModelAndView("redirect:addStudent.html");
	}


@RequestMapping(value = "/addClass.html", method = RequestMethod.GET)

public ModelAndView classLoad()
{

	return new ModelAndView("Admin/addClass","class",new classVO());
}


@RequestMapping(value = "/classcontroller.html", method = RequestMethod.POST)
	public ModelAndView saveclass(HttpServletRequest request, @ModelAttribute classVO vo) 
	{
		
	this.classdao.insertclass(vo);
	return new ModelAndView("redirect:addClass.html");
	}

@RequestMapping(value = "/viewClass.html", method = RequestMethod.GET)
	public ModelAndView searchclass(HttpServletRequest request, @ModelAttribute classVO v) 
	{
		List classls = this.classdao.searchclass(v);
		return new ModelAndView("Admin/viewClass", "view", classls);
	}


@RequestMapping(value = "/viewStudent.html", method = RequestMethod.GET)
	public ModelAndView searchclass(HttpServletRequest request, @ModelAttribute registerVO v) 
	{
		List ls = this.dao.searchStudent(v);
		return new ModelAndView("Admin/viewStudent", "viewStudent", ls);
	}
}
