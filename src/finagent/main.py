#!/usr/bin/env python
from finagent.crew import finagent
from dotenv import load_dotenv
#import streamlit as st
load_dotenv()



def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'topic': '"I want to start saving for college/university. What are the best options available to me, and how much should I be setting aside?"
    }
    finagent().crew().kickoff(inputs=inputs)