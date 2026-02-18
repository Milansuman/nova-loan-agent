import {
  ArrowRight,
  Shield,
  TrendingUp,
  CreditCard,
  Landmark,
  PhoneCall,
  Globe,
} from "lucide-react";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
  CardContent,
} from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Separator } from "@/components/ui/separator";

const features = [
  {
    icon: Shield,
    title: "Secure Banking",
    description:
      "Enterprise-grade encryption and multi-factor authentication keep your money safe around the clock.",
  },
  {
    icon: TrendingUp,
    title: "Smart Investments",
    description:
      "AI-powered insights help you grow your wealth with personalized portfolio recommendations.",
  },
  {
    icon: CreditCard,
    title: "Rewarding Cards",
    description:
      "Earn cashback, travel points, and exclusive perks with every purchase you make.",
  },
  {
    icon: Globe,
    title: "Global Transfers",
    description:
      "Send and receive money worldwide with low fees and real-time exchange rates.",
  },
];

const stats = [
  { value: "2M+", label: "Active Customers" },
  { value: "$48B", label: "Assets Managed" },
  { value: "99.9%", label: "Uptime Guarantee" },
  { value: "150+", label: "Branch Locations" },
];

const products = [
  {
    title: "Personal Checking",
    description: "Zero-fee everyday banking with cashback rewards.",
    badge: "Popular",
    rate: "0.50% APY",
  },
  {
    title: "High-Yield Savings",
    description: "Grow your savings with our market-leading interest rates.",
    badge: "Best Rate",
    rate: "4.75% APY",
  },
  {
    title: "Home Loans",
    description: "Competitive mortgage rates to help you own your dream home.",
    badge: null,
    rate: "From 5.99%",
  },
];

export default function Home() {
  return (
    <div className="min-h-screen bg-background text-foreground font-sans">
      {/* Navigation */}
      <header className="sticky top-0 z-50 border-b border-border bg-background/80 backdrop-blur-md">
        <div className="mx-auto flex h-16 max-w-6xl items-center justify-between px-6">
          <div className="flex items-center gap-2">
            <Landmark className="size-6 text-primary" />
            <span className="text-xl font-bold tracking-tight">
              Meridian Bank
            </span>
          </div>
          <nav className="hidden items-center gap-6 text-sm font-medium text-muted-foreground md:flex">
            <a href="#features" className="transition-colors hover:text-foreground">
              Features
            </a>
            <a href="#products" className="transition-colors hover:text-foreground">
              Products
            </a>
            <a href="#about" className="transition-colors hover:text-foreground">
              About
            </a>
            <a href="#contact" className="transition-colors hover:text-foreground">
              Contact
            </a>
          </nav>
          <div className="flex items-center gap-3">
            <Button variant="ghost" size="sm">
              Log In
            </Button>
            <Button size="sm">Open Account</Button>
          </div>
        </div>
      </header>

      {/* Hero */}
      <section className="relative overflow-hidden">
        <div className="absolute inset-0 -z-10 bg-linear-to-b from-primary/5 to-transparent" />
        <div className="mx-auto max-w-6xl px-6 py-28 md:py-40">
          <div className="flex flex-col items-center text-center">
            <Badge variant="secondary" className="mb-6">
              Trusted by over 2 million customers
            </Badge>
            <h1 className="max-w-3xl text-4xl font-bold leading-tight tracking-tight md:text-6xl md:leading-[1.1]">
              Banking that moves{" "}
              <span className="text-primary">at your pace</span>
            </h1>
            <p className="mt-6 max-w-xl text-lg text-muted-foreground">
              Experience seamless personal and business banking with
              Meridian&nbsp;Bank. Smarter tools, better rates, and a team that
              puts you first.
            </p>
            <div className="mt-10 flex flex-col gap-4 sm:flex-row">
              <Button size="lg" className="gap-2">
                Get Started <ArrowRight className="size-4" />
              </Button>
              <Button size="lg" variant="outline">
                Talk to an Advisor
              </Button>
            </div>
          </div>
        </div>
      </section>

      {/* Stats */}
      <section className="border-y border-border bg-muted/40">
        <div className="mx-auto grid max-w-6xl grid-cols-2 gap-8 px-6 py-12 md:grid-cols-4">
          {stats.map((stat) => (
            <div key={stat.label} className="flex flex-col items-center gap-1 text-center">
              <span className="text-3xl font-bold text-primary">
                {stat.value}
              </span>
              <span className="text-sm text-muted-foreground">
                {stat.label}
              </span>
            </div>
          ))}
        </div>
      </section>

      {/* Features */}
      <section id="features" className="mx-auto max-w-6xl px-6 py-24">
        <div className="mb-14 text-center">
          <h2 className="text-3xl font-bold tracking-tight md:text-4xl">
            Why choose Meridian&nbsp;Bank?
          </h2>
          <p className="mx-auto mt-4 max-w-lg text-muted-foreground">
            Modern banking features designed to simplify your financial life and
            help you achieve your goals.
          </p>
        </div>
        <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
          {features.map((feature) => (
            <Card
              key={feature.title}
              className="transition-shadow hover:shadow-md"
            >
              <CardHeader>
                <div className="mb-2 flex size-10 items-center justify-center rounded-lg bg-primary/10">
                  <feature.icon className="size-5 text-primary" />
                </div>
                <CardTitle className="text-base">{feature.title}</CardTitle>
                <CardDescription>{feature.description}</CardDescription>
              </CardHeader>
            </Card>
          ))}
        </div>
      </section>

      {/* Products */}
      <section id="products" className="border-t border-border bg-muted/30">
        <div className="mx-auto max-w-6xl px-6 py-24">
          <div className="mb-14 text-center">
            <h2 className="text-3xl font-bold tracking-tight md:text-4xl">
              Products tailored for you
            </h2>
            <p className="mx-auto mt-4 max-w-lg text-muted-foreground">
              Whether you&apos;re saving, spending, or borrowing — we have the
              right product at the right rate.
            </p>
          </div>
          <div className="grid gap-6 md:grid-cols-3">
            {products.map((product) => (
              <Card
                key={product.title}
                className="flex flex-col justify-between transition-shadow hover:shadow-md"
              >
                <CardHeader>
                  <div className="flex items-center gap-2">
                    <CardTitle className="text-lg">{product.title}</CardTitle>
                    {product.badge && (
                      <Badge variant="secondary" className="text-[10px]">
                        {product.badge}
                      </Badge>
                    )}
                  </div>
                  <CardDescription>{product.description}</CardDescription>
                </CardHeader>
                <CardContent className="flex items-center justify-between">
                  <span className="text-2xl font-bold text-primary">
                    {product.rate}
                  </span>
                  <Button variant="outline" size="sm" className="gap-1">
                    Learn more <ArrowRight className="size-3" />
                  </Button>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="mx-auto max-w-6xl px-6 py-24">
        <Card className="bg-primary text-primary-foreground">
          <CardContent className="flex flex-col items-center gap-6 py-12 text-center">
            <h2 className="text-3xl font-bold tracking-tight md:text-4xl">
              Ready to bank smarter?
            </h2>
            <p className="max-w-md text-primary-foreground/80">
              Open a Meridian Bank account in minutes. No paperwork, no
              branches, no hassle.
            </p>
            <div className="flex flex-col gap-3 sm:flex-row">
              <Button
                size="lg"
                variant="secondary"
                className="gap-2"
              >
                Open an Account <ArrowRight className="size-4" />
              </Button>
              <Button
                size="lg"
                variant="outline"
                className="border-primary-foreground/30 text-foreground hover:text-primary-foreground hover:bg-primary-foreground/10 gap-2"
              >
                <PhoneCall className="size-4" /> Contact Us
              </Button>
            </div>
          </CardContent>
        </Card>
      </section>

      <Separator />

      {/* Footer */}
      <footer id="contact" className="border-t border-border bg-muted/30">
        <div className="mx-auto max-w-6xl px-6 py-12">
          <div className="grid gap-10 sm:grid-cols-2 md:grid-cols-4">
            <div>
              <div className="mb-4 flex items-center gap-2">
                <Landmark className="size-5 text-primary" />
                <span className="font-semibold">Meridian Bank</span>
              </div>
              <p className="text-sm text-muted-foreground">
                Banking reimagined for the modern world. FDIC insured.
              </p>
            </div>
            <div>
              <h4 className="mb-3 text-sm font-semibold">Products</h4>
              <ul className="space-y-2 text-sm text-muted-foreground">
                <li><a href="#" className="hover:text-foreground">Checking</a></li>
                <li><a href="#" className="hover:text-foreground">Savings</a></li>
                <li><a href="#" className="hover:text-foreground">Credit Cards</a></li>
                <li><a href="#" className="hover:text-foreground">Loans</a></li>
              </ul>
            </div>
            <div>
              <h4 className="mb-3 text-sm font-semibold">Company</h4>
              <ul className="space-y-2 text-sm text-muted-foreground">
                <li><a href="#" className="hover:text-foreground">About</a></li>
                <li><a href="#" className="hover:text-foreground">Careers</a></li>
                <li><a href="#" className="hover:text-foreground">Press</a></li>
                <li><a href="#" className="hover:text-foreground">Blog</a></li>
              </ul>
            </div>
            <div>
              <h4 className="mb-3 text-sm font-semibold">Support</h4>
              <ul className="space-y-2 text-sm text-muted-foreground">
                <li><a href="#" className="hover:text-foreground">Help Center</a></li>
                <li><a href="#" className="hover:text-foreground">Security</a></li>
                <li><a href="#" className="hover:text-foreground">Privacy</a></li>
                <li><a href="#" className="hover:text-foreground">Terms</a></li>
              </ul>
            </div>
          </div>
          <Separator className="my-8" />
          <p className="text-center text-xs text-muted-foreground">
            &copy; 2026 Meridian Bank. All rights reserved. Member FDIC.
          </p>
        </div>
      </footer>
    </div>
  );
}
