purpose of statistics
inferrential statistics



inferrential statisitics-> Claim (hypothesis) -> Mobile manufacture promisiong 96% battery life. how they tested it.
Ex: Car dealer age 30-35  who to pay attention to > how he measured it age is 30-35 person will buy a car.

how they confirmed- is find the average of n number of batteries and show case the average value of it.


population - Sampling used for finding the average 
mew = average 
pi =  claim 10% of batter willl fail. % of time failure will occured
sigma square - variance 

sample statistics. 
X bar -> Mew - claim -> sample of (N)
P hat -> proportion of the sample (pihat)
s square - variance in sample 

method of sample and size of sample is important to inference.
suggested method is random sampling method.

Sampling distribution

population N=5 
[1,2,3,7,9]: mean mew = 5,  variance sigma square = 8


More on CLT
Central limit theorem
>> 

Sampling distribution - proportion
#toss of a coin  2^5 = 32 possibilities
pr(H) = p = 0.5 
pr(T) = q = 0.5
toss 5 times 

binomial distribution function.
p(x) = c(n,x) p^x * q^n-x 

if n>30
mew = np
sigma square = npq

Binomial distribution vs nominal distribution

================
confidence interval
>> point and range estimates
point estimates> mobile - 96 hours brattery life. sample = 94 hrs = Mew
x bar = mew + root of 1.96 * sigma / square root of n

Range estimate



=================================================
hypothesis testing 

hypothesis meaning > based on knowledge giving confidence based on the existing work.
basis of reasoninig without knowing the truth.

conducting the hypothesis below 4 points are required.
 1. Statement of Hypotheses
- Null Hypothesis (H₀): The battery life is equal to 96 hours.
H_0:\mu =96
- Alternate Hypothesis (H₁): The battery life is not equal to 96 hours.
H_1:\mu \neq 96
(This is a two-tailed test since we’re checking for “not equal.”)

🔹 2. Alpha Value (Significance Level)
- This is the threshold for deciding whether to reject the null hypothesis.
- Common choices: \alpha =0.05 (5%) or \alpha =0.01 (1%).
- Example: If \alpha =0.05, we’re allowing a 5% chance of rejecting H_0 when it’s actually true.

🔹 3. Test Statistic
- The test statistic compares the sample mean (\bar {x}) to the hypothesized mean (\mu _0).
- Formula (for a z-test when population variance is known):
z=\frac{\bar {x}-\mu _0}{\sigma /\sqrt{n}}
- If variance is unknown, we use a t-test:
t=\frac{\bar {x}-\mu _0}{s/\sqrt{n}}
where:
- \bar {x} = sample mean
- \mu _0 = hypothesized mean (96 hrs)
- \sigma  or s = population or sample standard deviation
- n = sample size

🔹 4. P-Value
- The p-value is the probability of observing a test statistic as extreme as the one calculated, assuming H_0 is true.
- Decision rule:
- If p\leq \alpha  → Reject H_0 (evidence battery life ≠ 96 hrs).
- If p>\alpha  → Fail to reject H_0 (no evidence against 96 hrs).

✅ So in practice, you’d:
- State H_0 and H_1.
- Choose \alpha .
- Compute the test statistic using your sample data.
- Find the p-value and compare it with \alpha .
================================================================

coin toss - 50 times
p= probability should be between 0.1 to 0.5
alpha 
beta - when null hypothesis value is true . 

================
Hypothesis Testing procedure
1) Find what you are going to test
mean (Average)
proportion
variance
Coefficient regression

2) convert business question into Hypothesis Ex: mew =96 hrs or mew  not eq  96 hrs
3) test statistics:
sample count, against the population
4) max risk to take for rejection the null hypothesis > alpha
5) Threshold.

VARIable = pi

tests 
Binomial Test
one sample Test
ZTest
T Test(with Ftest)
mcNemar Test
t test

=====================
Example of Hypotheses Test
Question:
>>> 3 years back uesd car is 6000 dollar whether that is changed now ??? 
1) one sample test for mean
    Hypothesis 
        H0: mew = 6000
        H1: mew not = 6000
    Sample statistics
        x bar : S sample used for estimation
    Test statisitics
        t Value
    Max uncertainity:
        alpha: 0.05
    computed uncertainity:
        p = 0.4
    Decision on H0:
        Donot reject null Hypothesis conclude mew =6000

| Sample size |  Sample staticss | Test | Test Statistics | P value |
| 1000        | mean= $6118.34   | tTest| 0.81            | 04      |

Question:
3 years back % of used car with automatic tramission were 23% has it changed now??
2) one sample test for proportion
    Hypothesis 
        H0: PI = .23
        HA: PI not = .23
    Sample statistics
        p hat: H0 is used to compute sigma 
    Test statisitics
        z Value
    Max uncertainity:
        alpha: 0.05
    computed uncertainity:
        p = 0.22
    Decision on H0:
        Donot reject null Hypothesis conclude PI  =.23

| Sample size |  Sample staticss                   | Test | Test Statistics | P value |
| 1000        | prop of automatically gear =.214   | zTest| 0.81            | 0.22      |

Question: 
what happens in price of car that have run 30000 - 60000Km, the same as that for cars that have run 70000-90000Km??? 
two sub group created above - two independent groups 
3) Two sample test for means
  Hypothesis 
        H0: mew1  = mew2
        HA: mew1 not = mew2
    Sample statistics
        x bar : S is being used to estimate of sigma
    Test statisitics
        two gorup are equal or unequal is measured. based on the group formula will changed.
            1) F test = F value
            2) welch t statistics for unequal variances.
    Max uncertainity:
        alpha: 0.05
    computed uncertainity:
        p = 0.00
    Decision on H0:
        Reject null Hypothesis H0 = sigma 1 squrae not equal sigma 2 square. 

4) Two sample test for proportion
Question:
Propotion petrol cars in two different time periods (2009-2013 and 2014-2018) ?? 
>>> Percentage will be calculated.

Hypothesis 
        H0: pi1  = pi2
        HA: pi1 not = pi2
    Sample statistics
        p hat > diffenert group > pooled estimate of phat is used to estimate sigma
    Test statisitics
        z value
    Max uncertainity:
        alpha: 0.05
    computed uncertainity:
        p = 0.59
    Decision on H0:
        Do not Reject null Hypothesis conclude pi1 = pi2



===========================================================
DISTRIBUTION in PYTHON

1) Random Variable.
> map outcome of sample same to a real number. ex: H/T maps to 0/1
2) probability mass/density function
> probabilitymass function assigns to probability measure to every discrete outcome of sample space.
EX: coin toss - H/T which is 0/1 so discrete random vairable outcome is p(X=0)=0.5 and p(X=1)=0.5 
discrete - probability mass function
Continuous random variable - probability density function. (f(x)) 

3) cumulative distribution/Density function
> This is the p() tjat the RV 'x' lies in the interval- infinity < x< b

common functionality in PYTHON
1) rvs - random number from a distribution
2) pdf - probability density function
3) cdf - cumulative distribution function
4) ppf - precentile point function (inverse cumulative distribution function)

distribution root name

norm - normal distribution
binom - binomial distrubtion.

standard normail distribution ie mean =0 sd=1
