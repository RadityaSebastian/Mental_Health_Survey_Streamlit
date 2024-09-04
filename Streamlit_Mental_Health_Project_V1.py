import pandas as pd
import numpy as np
import streamlit as st
import altair as alt
import plotly.express as px
#page configuration
st.set_page_config(
    page_title="Mental Health Survey",
    page_icon="👨🏻‍⚕️",
    layout="wide",
    initial_sidebar_state="expanded")

#alt.themes.enable("dark")
#import data
data = pd.read_csv('MentalHealthSurvey_Clean.csv')
columns = data.columns
#page sidebar
with st.sidebar:
    st.title('Mental Health Survey')
    #university
    university_list = list(data.university.unique())[::-1]
    university_list.append("Every University")
    selected_university = st.selectbox('Select a university', university_list, index=len(university_list)-1)
    df_selected_university = data[data.university == selected_university]
    df_selected_university_sorted = df_selected_university.sort_values(by="age", ascending=False)

    #degree
    degree_list = list(data.degree_level.unique())[::-1]
    degree_list.append("Both")
    selected_degree = st.selectbox('Select a degree', degree_list, index=len(degree_list)-1)
    df_selected_degree = data[data.degree_level == selected_degree]
    df_selected_degree_sorted = df_selected_degree.sort_values(by="age", ascending=False)

    #major
    major_list = list(data.degree_major.unique())[::-1]
    major_list.append("All")
    selected_major = st.selectbox('Select a major', major_list, index=len(major_list)-1)
    df_selected_major = data[data.degree_major == selected_major]
    df_selected_major_sorted = df_selected_major.sort_values(by="age", ascending=False)


#condition code

# 1st condition
if selected_university !="Every University":
    data = data[data['university']==selected_university]
elif selected_degree !="Both":
    data = data[data['degree_level']==selected_degree]
elif selected_major !="All":
    data = data[data['degree_major']==selected_major]

#2nd condition
if selected_university !="Every University" and selected_degree !="Both":
    data = data[(data['university']==selected_university)&(data['degree_level']==selected_degree)]
elif selected_degree !="Both" and selected_major !="All":
    data = data[(data['degree_level']==selected_degree)&(data['degree_major']==selected_major)]
elif selected_university !="Every University" and selected_major !="All":
    data = data[(data['university']==selected_university)&(data['degree_major']==selected_major)]

#3rd condition
if selected_university !="Every University" and selected_degree !="Both" and selected_major!="All":
    data = data[(data['university']==selected_university)&(data['degree_level']==selected_degree)&(data['degree_major']==selected_major)]
#functions
def pie_chart_maker(df,names,values,category_names,y_title,x_title,hole_size,pie_color):
  if pie_color =="Teal":
    fig = px.pie(df, values=values, names=names, hole=hole_size,color_discrete_sequence=px.colors.sequential.Teal)
    fig.update_layout(
      title={
          'text': category_names,
          'y':y_title,
          'x':x_title,
          'xanchor': 'center',
          'yanchor': 'top'},

      )
  elif pie_color =="Burg":
    fig = px.pie(df, values=values, names=names, hole=hole_size,color_discrete_sequence=px.colors.sequential.Burg)
    fig.update_layout(
      title={
          'text': category_names,
          'y':y_title,
          'x':x_title,
          'xanchor': 'center',
          'yanchor': 'top'},

      )
  elif pie_color =="Purp":
    fig = px.pie(df, values=values, names=names, hole=hole_size,color_discrete_sequence=px.colors.sequential.Purp)
    fig.update_layout(
      title={
          'text': category_names,
          'y':y_title,
          'x':x_title,
          'xanchor': 'center',
          'yanchor': 'top'},

      )     
  return fig
def bar_chart_maker(df,names,values,category_names,y_title,x_title,color):
  fig = px.bar(df, x=names, y=values, color=values,color_continuous_scale=color)
  fig.update_layout(
    title={
      'text':category_names,
      'y':y_title,
      'x':x_title,
      'xanchor':'center',
      'yanchor':'top'
    }
  )
  return fig
def stress_relief_function(names,df,stress_values):
  for i in range(len(names)):
    if df[df["unique_values"]==names[i]].empty:
      stress_values[i]+=0
    else:
      for j in range(len(df)):
        if names[i]==df['unique_values'].values[j]:
          stress_values[i]+=df['counts'].values[j]
  return stress_values
#main code
if data.empty:
    st.markdown('#### Sorry, there is no data within that category')
    
else:
    stress_values = [0,0,0,0,0,0,0,0]
    #st.write(data)
    gender_data =data['gender'].value_counts().rename_axis('gender').reset_index(name='Total')
    age_data =data['age'].value_counts().rename_axis('Age').reset_index(name='Total')
    cgpa_data = data['cgpa'].value_counts().rename_axis('gpa').reset_index(name="Total")
    sports_data = data['sports_engagement'].value_counts().rename_axis('sports').reset_index(name="Total")
    sleep_data = data['average_sleep'].value_counts().rename_axis('sleep').reset_index(name="Total")
    satisfy_data = data['study_satisfaction'].value_counts().rename_axis('satisfy').reset_index(name="Total")
    workload_data = data['academic_workload '].value_counts().rename_axis('workload').reset_index(name="Total")
    pressure_data = data['academic_pressure'].value_counts().rename_axis('pressure').reset_index(name="Total")
    financial_data = data['financial_concerns'].value_counts().rename_axis('financial').reset_index(name="Total")
    relationship_data = data['social_relationships'].value_counts().rename_axis('relationship').reset_index(name="Total")
    depression_data = data['depression'].value_counts().rename_axis('depression').reset_index(name="Total")
    anxiety_data = data['anxiety'].value_counts().rename_axis('anxiety').reset_index(name="Total")
    isolation_data = data['isolation'].value_counts().rename_axis('isolation').reset_index(name="Total")
    future_insecurity_data = data['future_insecurity'].value_counts().rename_axis('insecurity').reset_index(name="Total")
    df_val =data['Item1'].value_counts().rename_axis('unique_values').reset_index(name='counts')
    df_val2 =data['Item2'].value_counts().rename_axis('unique_values').reset_index(name='counts')
    df_val3 = data["Item3"].value_counts().rename_axis('unique_values').reset_index(name='counts')
    df_val4 = data["Item4"].value_counts().rename_axis('unique_values').reset_index(name='counts')
    df_val5 = data["Item5"].value_counts().rename_axis('unique_values').reset_index(name='counts')
    df_val6 = data["Item6"].value_counts().rename_axis('unique_values').reset_index(name='counts')
    
    names = ["Religious Activities","Online Entertainment","Social Connections","Sports and Fitness","Nothing","Outdoor Activities","Sleep","Creative Outlets"]
    test = stress_relief_function(names,df_val,stress_values)
    test = stress_relief_function(names,df_val2,stress_values)
    test = stress_relief_function(names,df_val3,stress_values)
    test = stress_relief_function(names,df_val4,stress_values)
    test = stress_relief_function(names,df_val5,stress_values)
    test = stress_relief_function(names,df_val6,stress_values)
    col = st.columns((1.5, 4.5, 2), gap='medium')
    #column management
    with col[0]:
      st.markdown('#### Gender Graph')
      Gender_graph_color_option = st.selectbox(
    "Gender Graph Color:",
    ("Teal","Purp","Burg"),key="Genders"
    )
      gender_chart = pie_chart_maker(gender_data,'gender','Total',"<b>Student Gender</b>",0.75,0.35,.2,Gender_graph_color_option)
      st.plotly_chart(gender_chart, use_container_width=True)
      st.markdown('#### Age Graph')
      graph_color_option = st.selectbox(
    "Age Graph Color:",
    ("bluered","tealgrn","teal","sunsetdark","sunset","haline","thermal","agsunset","blues","greys"),key="ages"
    )
      age_chart = bar_chart_maker(age_data,'Age','Total','<b>Student Age</b>',0.9,0.45,graph_color_option)
      st.plotly_chart(age_chart, use_container_width=True)
      st.markdown('### GPA')
      GPA_graph_color_option = st.selectbox(
    "GPA Graph Color:",
    ("Teal","Purp","Burg"),key="GPAs"
    )
      gpa_chart = pie_chart_maker(cgpa_data,'gpa','Total','<b>Student GPA</b>',0.8,0.4,.5,GPA_graph_color_option)
      st.plotly_chart(gpa_chart,use_container_width=True)
    with col[1]:
      st.markdown('### Stress')
      Stress_color_option = st.selectbox(
    "Stress Graph Color:",
    ("bluered","tealgrn","teal","sunsetdark","sunset","haline","thermal","agsunset","blues","greys"),key=" Stress"
    )
      Stress_option = st.selectbox(
    "Things that affect student Mental Health:",
    ("study satisfaction","academic workload","academic pressure","financial problem","social relationship","depression","anxiety","isolation","future insecurity"),key=" Stress_Type"
    )
      if Stress_option =="study satisfaction":
        satisfy_chart = bar_chart_maker(satisfy_data,'satisfy','Total','<b>Student Satisfaction </b>',0.9,0.45,Stress_color_option)
        satisfy_chart.update_layout(xaxis_title=None)
        st.plotly_chart(satisfy_chart, use_container_width=True)
      elif Stress_option =="academic workload":
        workload_chart = bar_chart_maker(workload_data,'workload','Total','<b>Academic Workload </b>',0.9,0.45,Stress_color_option)
        workload_chart.update_layout(xaxis_title=None)
        st.plotly_chart(workload_chart, use_container_width=True)
      elif Stress_option =="academic pressure":
        pressure_chart = bar_chart_maker(pressure_data,'pressure','Total','<b>Academic Pressure </b>',0.9,0.45,Stress_color_option)
        pressure_chart.update_layout(xaxis_title=None)
        st.plotly_chart(pressure_chart, use_container_width=True)
      elif Stress_option =="financial problem":
        financial_chart = bar_chart_maker(financial_data,'financial','Total','<b>Financial Problem </b>',0.9,0.45,Stress_color_option)
        financial_chart.update_layout(xaxis_title=None)
        st.plotly_chart(financial_chart, use_container_width=True)
      elif Stress_option =="social relationship":
        relationship_chart = bar_chart_maker(relationship_data,'relationship','Total','<b>Social Relationship</b>',0.9,0.45,Stress_color_option)
        relationship_chart.update_layout(xaxis_title=None)
        st.plotly_chart(relationship_chart, use_container_width=True)
      elif Stress_option =="depression":
        depression_chart = bar_chart_maker(depression_data,'depression','Total','<b>Depression</b>',0.9,0.45,Stress_color_option)
        depression_chart.update_layout(xaxis_title=None)
        st.plotly_chart(depression_chart, use_container_width=True)
      elif Stress_option =="anxiety":
        anxiety_chart = bar_chart_maker(anxiety_data,'anxiety','Total','<b>Anxiety</b>',0.9,0.45,Stress_color_option)
        anxiety_chart.update_layout(xaxis_title=None)
        st.plotly_chart(anxiety_chart, use_container_width=True)
      elif Stress_option =="isolation":
        isolation_chart = bar_chart_maker(isolation_data,'isolation','Total','<b>Isolation</b>',0.9,0.45,Stress_color_option)
        isolation_chart.update_layout(xaxis_title=None)
        st.plotly_chart(isolation_chart, use_container_width=True)
      elif Stress_option =="future insecurity":
        insecurity_chart = bar_chart_maker(future_insecurity_data,'insecurity','Total','<b>Future Insecurity</b>',0.9,0.45,Stress_color_option)
        insecurity_chart.update_layout(xaxis_title=None)
        st.plotly_chart(insecurity_chart, use_container_width=True)                                   
    with col[2]:
      st.markdown("### Sports Graph")
      sports_color_option = st.selectbox(
    "Sports Graph Color:",
    ("bluered","tealgrn","teal","sunsetdark","sunset","haline","thermal","agsunset","blues","greys"),key="sports"
    )
      sports_chart = bar_chart_maker(sports_data,'sports','Total','<b>Frequency Student Exercise </b>',0.9,0.45,sports_color_option)
      st.plotly_chart(sports_chart, use_container_width=True)
      st.markdown("### Sleep Graph")
      sleep_color_option = st.selectbox(
    "Sleep Graph Color:",
    ("bluered","tealgrn","teal","sunsetdark","sunset","haline","thermal","agsunset","blues","greys"),key="sleep"
    )
      sleep_chart = bar_chart_maker(sleep_data,'sleep','Total','<b>Frequency Student Exercise </b>',0.9,0.45,sleep_color_option)
      st.plotly_chart(sleep_chart, use_container_width=True)
      st.markdown("### Stress Relief Activity")
      Relief_color_option = st.selectbox(
    "Stress Relief Activity Graph Color:",
    ("bluered","tealgrn","teal","sunsetdark","sunset","haline","thermal","agsunset","blues","greys"),key="relief"
    )
      fig_relief = px.bar(y=names,x=test, color=test,color_continuous_scale=Relief_color_option)
      fig_relief.update_layout(
          title={
              'text': "<b>Activity That Student Used to Decressed Stress</b>",
              'y':0.95,
              'x':0.5,
              'xanchor': 'center',
              'yanchor': 'top'},
          xaxis_title="Activities",
          yaxis_title="Category"
          )
      fig_relief.update_layout(
          xaxis=dict(showgrid=False,zeroline=False),
          yaxis=dict(showgrid=False)
      )
      fig_relief.update_traces(width=0.35)

      st.plotly_chart(fig_relief, use_container_width=True)
      st.write("###### Credit to the Data is used for this project: https://www.kaggle.com/datasets/abdullahashfaqvirk/student-mental-health-survey/data")
